# Poetry usage

+ [Install poetry](#install-poetry)
+ [Initialization](#initialization)
+ [Adding packages](#adding-packages)
+ [Entering virtual environment](#enter-virtual-environment)

## Install poetry

To install poetry it is possible to use homebrew or pip3.

To install via homebrew:

```bash
brew install poetry
```

To install via pip3:

```bash
pip3 install poetry
```

## Initialization

If pyproject.toml is not given in directory, but you want use it, just use this command to initialize poetry:

```bash
poetry init
```

The installer will ask you to specify project settings, you can configure them as you wish.

## Adding packages

You can add all the packages by this command (you need to ensure that there is no unnecessary symbols inside)

```bash
poetry add $( cat requirements.txt )
```

Or if you have some symbols you can try:

```bash
poetry add $(sed -e 's/#.*//' -e '/^$/ d' < requirements.txt)
```

Or you can add packages manually one by one:

```bash
poetry add kfp
```

## Entering virtual environment

If everything is set for you can enter virtual environment:

```bash
poetry shell
```
Moreover, it is possible to change pyproject.toml, expand it. See official page: https://python-poetry.org/
