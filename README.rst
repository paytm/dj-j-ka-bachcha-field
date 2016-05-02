====================
Dj jkabachcha field
====================

Dj jkabachcha is a Django app to create Json WYSIWYG field for Django models.

Quick start
-----------

1. Add "jkbachcha" to your INSTALLED_APPS like this::

    ```
    INSTALLED_APPS = (
        ...
        'jkbachcha',
    )
    ```

2. Import it in your models like::

    ```
    from myghanta.db.fields import JsonField
    ```

3. Create model fields like::

    ```
       json_text = JsonField()
    ```

4. Use widget to override default Textarea in ModelAdmin class like::

    ```
        # import widget
        from jkbachcha.forms.widgets import JsonTextWidget
        
        # in ModelAdmin class, like

        formfield_overrides = {
            models.TextField : {'widget': JsonTextWidget},
        }
    ```