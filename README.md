# dj-jkabachcha-field

[![PyPI version](https://badge.fury.io/py/dj-jkabachcha.svg)](https://badge.fury.io/py/dj-jkabachcha) [![Build Status](https://travis-ci.org/paytm/dj-j-ka-bachcha-field.svg?branch=master)](https://travis-ci.org/paytm/dj-j-ka-bachcha-field)

Django J(son) field is a package to create Json WYSIWYG model field. This is mainly to have a cool editable view in Admin. The package ships with a model field which has its widget as a Json WYSIYG. It also provides a widget which can be independently used to override existing model fields which are using TextArea. Overall there can be two ways 

    * As a ModelField
    * As a Widget

## Installation

* Install it through pip
    ```
    pip install dj-jkabachcha
    ```

* Download and install manually

    ```
    git clone https://github.com/paytm/dj-j-ka-bachcha-field.git
    cd dj-j-ka-bachcha-field
    python setup.py install
    ```

## Use

* Add `jkabachcha` in your `INSTALLED_APPS` like

    ```
    INSTALLED_APPS = (
        ...
        'jkabachcha',
    )
    ```

* Collect static files by running

    ```
    python manage.py collectstatic
    ```

* Now import it in your models like

    ```
    from jkabachcha.db.fields import JsonField
    ```

* Create fields like

    ```
    json_text = JsonField()
    ```
* This can be used as a widget to override __TextArea__ in Admin panel like

    ```
    # import widget
    from jkabachcha.forms.widgets import JsonTextWidget

    # in ModelAdmin class, like

    formfield_overrides = {
        models.TextField : {'widget': JsonTextWidget},
    }
    ```

## Note

While using this field, if asked for default value while running `makemigrations`, make sure that you specify the value as empty string
`''`. This is necessary to prevent unhasable dict type error.

## Screenshots

* Empty Json Object

    ![Empty Json Object](https://github.com/paytm/dj-j-ka-bachcha-field/blob/master/.snaps/empty_object.png "Empty Json Object")

* Json Object

    ![Empty Object](https://github.com/paytm/dj-j-ka-bachcha-field/blob/master/.snaps/object_json.png "Empty Object")

* Raw Textarea

    ![Raw Textarea](https://github.com/paytm/dj-j-ka-bachcha-field/blob/master/.snaps/object_textarea.png "Raw Textarea")


## Credits

This package uses [jsoneditor](https://github.com/josdejong/jsoneditor) and [jquery](https://github.com/jquery/jquery) as its dependency.