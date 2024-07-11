# Cacheasy

This is a simple utility Python package for caching Python objects. Makes use of the `pickle` standard library and simply stores files in a folder called `cache`. If you want to use another location, you can specify `cache_folderpath` in a `.env` file.

## Writing to cache

```python
import cacheasy
x = 5
cacheasy.write_to_cache(x, 'my_cool_x')
```

## Reading from cache

```python
import cacheasy
x = cacheasy.read_from_cache('my_cool_x')
```

## Common usage

A common work flow is to check if a file is in the cache, if it is not to create it and write to cache, if the file is in cache you read it:

```python
import cacheasy
x_cache_filepath = 'my_cool_x'
if cacheasy.file_in_cache(x_cache_filepath):
    x = cacheasy.read_from_cache(x_cache_filepath)
else:
    x = 5
    cacheasy.write_to_cache(x_cache_filepath)
```

## Removing from cache

```python
import cacheasy
cacheasy.remove_from_cache('my_cool_x')
```

Or if you want to remove all your cache, get the `cache_folderpath` and then remove it with the `shutil` library:

```python
import cacheasy
import shutil
shutil.rmtree(cacheasy.get_cache_folderpath())
```
