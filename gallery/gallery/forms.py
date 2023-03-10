from django import forms

from core.models import Gallary

class UploadImageForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for myField in self.fields:
        self.fields[myField].widget.attrs['class'] = 'form-control'
        self.fields[myField].widget.attrs['type'] = 'file'
  
  class Meta:
    model = Gallary
    fields = "__all__"
    exclude=('image_name','user_id',)

  def save(self, commit=True):
    gallery = super(UploadImageForm, self).save(commit=False)
    
    if commit:
      gallery.save()
    return gallery
