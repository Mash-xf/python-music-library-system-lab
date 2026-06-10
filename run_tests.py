#!/usr/bin/env python3
import importlib.util
import sys
import types
from pathlib import Path

TEST_PATH = Path(__file__).parent / 'lib' / 'testing' / 'song_test.py'

spec = importlib.util.spec_from_file_location('song_test', TEST_PATH)
module = importlib.util.module_from_spec(spec)
# Ensure the project's `lib` directory is on sys.path so `from song import Song` works
lib_dir = str(Path(__file__).parent / 'lib')
if lib_dir not in sys.path:
    sys.path.insert(0, lib_dir)

spec.loader.exec_module(module)

TestSong = getattr(module, 'TestSong')

 # Run any method that starts with test_ in source order
instance = TestSong()
failures = []
from song import Song

print('INITIAL SONG STATE:')
print('count=', Song.count)
print('artists=', Song.artists)
print('genres=', Song.genres)
print('artist_count=', Song.artist_count)
print('genre_count=', Song.genre_count)
print('all len=', len(Song.all))

# Determine test order by parsing the source file for defs inside the TestSong class
source = TEST_PATH.read_text()
test_names = []
in_class = False
for line in source.splitlines():
    stripped = line.strip()
    if stripped.startswith('class TestSong'):
        in_class = True
        continue
    if in_class:
        if stripped.startswith('def test_'):
            # def test_xxx(self):
            name = stripped.split('def ')[1].split('(')[0]
            test_names.append(name)
        # stop if next class or EOF
        if stripped.startswith('class ') and not stripped.startswith('class TestSong'):
            break

for name in test_names:
    try:
        getattr(instance, name)()
        print(f'PASS: {name}')
        print('  after PASS state:')
        print('   count=', Song.count)
        print('   artists=', Song.artists)
        print('   genres=', Song.genres)
        print('   artist_count=', Song.artist_count)
        print('   genre_count=', Song.genre_count)
        print('   all len=', len(Song.all))
    except AssertionError as e:
        print(f'FAIL: {name} - {e}')
        failures.append(name)
    except Exception as e:
        print(f'ERROR: {name} - {e}')
        failures.append(name)

if failures:
    print(f"\n{len(failures)} tests failed: {failures}")
    sys.exit(1)
else:
    print('\nAll tests passed')
    sys.exit(0)
