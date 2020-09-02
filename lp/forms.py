from django import forms

from . models import LeaveReply







class LeaveReplyForm(forms.ModelForm):

        class Meta:
                model = LeaveReply
                fields = ('name', 'email', 'comment')


                widgets = {
                        
                'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: medium', 'placeholder':'Name...'}),
                'email': forms.TextInput(attrs={'class': 'form-control', 'style': 'font-size: medium', 'placeholder':'Email...'}),

                'comment': forms.Textarea(attrs={'class': 'form-control', 'style': 'font-size: medium', 'placeholder':'Comment here...'}),
 }    



