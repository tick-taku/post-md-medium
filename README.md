# Post markdown to Medium

Post your markdown or text file to Medium.

## Usage

### for iPad

1.
Copy to integration token from Medium settings.


2.

```
python etc/init.py

integration token: <Your integration token here.>
```

```
./etc/init.sh

integration token: <Your integration token here.>
```

3.

```
python post_medium.py

file: <Your text file here.>
publishStatus: <draft or public>
```

- If you get `No module requests` error, try this

```
pip install requests
```


### Others

1.
Copy to integration token from Medium settings.


2.

```
./etc/init.sh

integration token: <Your integration token here.>
```

3.

```
pipenv run start

file: <Your text file here.>
publishStatus: <draft or public>
```
