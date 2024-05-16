[![Coverage Status](https://coveralls.io/repos/github/boterop/html2object/badge.svg?branch=main)](https://coveralls.io/github/boterop/html2object?branch=main)

# HTML 2 Object

Tools to handle the CRUD of .html files as objects.

## Install

```sh
pip install html2object
```

## Functions

- Parse your html file

  ```py
  html = open(<path>, "r").read("bin/gui/index.html")
  document = HtmlElement(html)
  ```

- Add attributes

  ```py
  document.add_attribute("class", "flex pt-2")
  ```

- Add children

  ```py
  p = HtmlElement(name="p").add_child("This is a text")
  document.add_child(p)
  ```

- Set new children

  ```py
  p = HtmlElement(name="p").add_child("This is a text")
  document.set_children([p])
  ```

- Get element by id

  ```py
  image = document.get_element_by_id("image_id")
  image.add_attribute("src", "image_url")
  ```

- Get element by id

  ```py
  images = document.get_elements_by_name("image")
  for image in images:
    url_list.append(image.get_attribute("src"))
  ```

## Usage

This project provides a way to manipulate HTML files and update them dynamically. Here's how you can use it:

First, import the necessary classes from this project:

```sh
from html2object import HtmlElement
```

read your html file and:

#### Create an `HtmlElement()`

```sh
html = open(<path>, "r").read("bin/gui/index.html")
document = HtmlElement(html)
```

#### Create scripts

```sh
update_script = HtmlElement(name="script").add_child(
    "setInterval(() => reload(), 1500);"
)
document.add_child(update_script)
```

#### Create a div

```sh
p = HtmlElement(name="p", id="textID").add_chil("Text")
div = HtmlElement(name="div").add_child(p)
document.add_child(div)
```

#### Use Document functions like JS

```sh
text_element = document.get_element_by_id("textID")
strong = HtmlElement(name="strong").add_child("Strong text")
text_element.set_child([strong, "No strong text"])
```

### save the html file running

```sh
open(path, "w").write(str(document)).close()
```

## Local setup

Instructions on how to install and set up your project. Include any dependencies that need to be installed.

1. Clone the repository
2. Navigate to the project directory:

```sh
cd html2object
```

3. Create a virtual environment (optional but recommended):

```sh
python3 -m venv venv
```

4. Activate the virtual environment:

- For Windows:

```sh
venv\Scripts\activate
```

- For macOS and Linux:

```sh
source venv/bin/activate
```

5. Install the project dependencies:

```sh
pip install -r requirements.txt
```

That's it! Your project should now be installed and ready to use.
