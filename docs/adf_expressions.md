# ADF Expressions Used in the Lab

## ForEach items

```text
@activity('Lookup_Control').output.value
```

## If condition for CSV

```text
@equals(item().source_format,'csv')
```

## Source dataset parameters for CSV

```text
folderPath = @item().source_folder
fileName   = @concat(item().source_entity,'.csv')
```

## Source dataset parameters for JSON

```text
folderPath = @item().source_folder
fileName   = @concat(item().source_entity,'.json')
```

## Sink dataset parameters

```text
folderPath = @item().sink_folder
```
