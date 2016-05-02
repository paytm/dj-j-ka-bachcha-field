====================
Dj jkabachcha field
====================

Dj jkabachcha is a Django app to create Json WYSIWYG field for Django models.

Quick start
-----------

1. Add "jkabachcha" to your INSTALLED_APPS like this::

    ```
    INSTALLED_APPS = (
        ...
        'jkabachcha',
    )
    ```

2. Import it in your models like::

    ```
    from jkabachcha.db.fields import JsonField
    ```

3. Create model fields like::

    ```
       json_text = JsonField()
    ```

4. Use widget to override default Textarea in ModelAdmin class like::

    ```
        # import widget
        from jkabachcha.forms.widgets import JsonTextWidget
        
        # in ModelAdmin class, like

        formfield_overrides = {
            models.TextField : {'widget': JsonTextWidget},
        }
    ```