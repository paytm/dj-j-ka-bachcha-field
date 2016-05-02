# dj-j-ka-bachcha-field
Django J(son) field is a package to create Json WYSIWYG model field. This is mainly to have a cool editable view in Admin

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

* Add `jkbachcha` in your `INSTALLED_APPS` like

    ```
    INSTALLED_APPS = (
        ...
        'jkbachcha',
    )
    ```

* Now import it in your models like

    ```
    from myghanta.db.fields import JsonField
    ```

* Create fields like

    ```
    json_text = JsonField()
    ```
* Also override existing textarea with this field, using widget like

    ```
    # import widget
    from jkbachcha.forms.widgets import JsonTextWidget

    # in ModelAdmin class, like

    formfield_overrides = {
        models.TextField : {'widget': JsonTextWidget},
    }
    ```

## Screenshots

* Empty Json Object

    ![Empty Json Object](https://github.com/paytm/dj-j-ka-bachcha-field/blob/master/.snaps/empty_object.png "Empty Json Object")

* Json Object

    ![Empty Object](https://github.com/paytm/dj-j-ka-bachcha-field/blob/master/.snaps/object_json.png "Empty Object")

* Raw Textarea

    ![Raw Textarea](https://github.com/paytm/dj-j-ka-bachcha-field/blob/master/.snaps/object_textarea.png "Raw Textarea")


## Credits

This package uses [jsoneditor](https://github.com/josdejong/jsoneditor) and [jquery](https://github.com/jquery/jquery) as its dependency.