from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        main_tags = [form.cleaned_data for form in self.forms if form.cleaned_data.get('is_main')]
        if len(main_tags) > 1:
            raise ValidationError('Only one main tag is allowed per article.')
        if len(main_tags) == 0:
            raise ValidationError('There must be one main tag for each article.')

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
