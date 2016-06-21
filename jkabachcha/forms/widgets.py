import json

from django.db import models
from django import forms

from django.templatetags.static import static
from django.utils.safestring import mark_safe

class JsonTextWidget(forms.widgets.Textarea):

    '''
        Json WYSIWYG widget, displays an empty json object,
        if no value is there
    '''

    def render(self, name, value, attrs=None):
        base_html = super(JsonTextWidget, self).render(name, value, attrs)
        if not value:
            value = '{}'

        # there is a possibility that value may not be a valid json
        # return empty json in that case, so that jsoneditor is
        # rendered properly
        try:
            json_object = json.loads(value)
        except ValueError as e:
            value = '{}'

        editor_html = '''
        <button style="float:right" id="button_%(name)s">Toggle</button>
        <div id="jsoneditor_%(name)s" style="width: auto; height: auto;"></div>
        <textarea cols="40" id="id_%(name)s" name="%(name)s" rows="10" style="display:none"></textarea>

        <script>
        // create the editor
        var container = document.getElementById("jsoneditor_%(name)s");
        
        var editor_%(name)s = new JSONEditor(container);

        // set json
        var jsonFor%(name)s = %(value)s ;
        editor_%(name)s.set(jsonFor%(name)s);

        $('#id_%(name)s').closest('form').submit(function(){
            var currentState = $("#id_%(name)s").css("display")==='none';
            if(currentState)
            {
                jsonFor%(name)s = editor_%(name)s.get();
                $('#id_%(name)s').val(JSON.stringify(jsonFor%(name)s));
            }
            });

        $('#button_%(name)s').on('click',function(event){
            event.preventDefault();
            $('#jsoneditor_%(name)s').toggle();
            var currentState = $("#id_%(name)s").css("display")==='none';
                if(currentState)
                {
                    $('#id_%(name)s').css('display','block');
                    jsonFor%(name)s = editor_%(name)s.get();
                    $('#id_%(name)s').val(JSON.stringify(jsonFor%(name)s, null, 4));
                }
                else{
                    $('#id_%(name)s').css('display','none');
                    jsonFor%(name)s = $('#id_%(name)s').val();
                    editor_%(name)s.set(JSON.parse(jsonFor%(name)s));
                }
        });
        </script>''' % {'name': name, 'value': value}
        return mark_safe(editor_html)

    class Media:
        css = {
            'all': ('jkabachcha/css/jsoneditor.min.css',)
        }
        js = ('jkabachcha/js/jquery.min.js', 
              'jkabachcha/js/jsoneditor.min.js', )
