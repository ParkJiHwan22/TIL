# 10. Django - Form

## 학습 목표

> Django Form과 ModelForm을 사용하여 사용자 입력 데이터를 수집하고 처리하는 방법을 이해할 수 있다.

> Django Form과 ModelForm의 개념과 차이점을 설명할 수 있다.

> ModelForm을 사용하여 데이터를 데이터베이스 모델과 연결하고 저장하는 방법을 작성할 수 있다.

> Form과 ModelForm에서 사용할 수 있는 다양한 필드 타입과 옵션을 활용할 수 있다.

# 1. 개요

### HTML form
- 사용자로부터 form 요소를 통해 데이터를 받고 있으나 비정상적 혹은 악의적인 요청을 확인하지 않고 모두 수용 중
- `우리가 원하는 데이터의 형식이 맞는지에 대한 '유효성 검증'필요`

### 유효성 검사
- 수집한 데이터가 정확하고 유효한지 확인하는 과정
- 유효성 검증에는 입력 값, 형식, 중복, 범위, 보안 등 부가적인 많은 것들을 고려해야 함
- 이런 과정과 기능을 제공해주는 `도구`가 필요

# 2. Django Form
- 사용자 입력 데이터를 수집하고, 처리 및 유효성 검증을 수행하기 위한 도구
- `유효성 검사를 단순화하고 자동화할 수 있는 기능을 제공`


### Form class 선언

``` python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
  title = forms.CharField(max_length=10)
  content = forms.CharField()
```

### Form class를 적용한 new 로직
``` python
# articles/views.py

from django import ArticleForm

class new(request):
  form = ArticleForm()
  context = {
    'form': form,
  }
  return render(request, 'articles/new.html', context)
```

### Form rendering options

``` HTML
<!-- articles/new.html -->

<h1>NEW</h1>
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_Token %}
  {{ form.as_p }} <!--  칸 나눔 -->
  <input type="submit">
</form>
```

# 3. Widgets

### Widgets
- HTML 'input' element의 표현을 담당
- 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것


``` python
# articles/forms.py

from django import forms

class ArticleForm(forms.Form):
  title = forms.CharField(max_length=10)
  content = forms.CharField(widget=forms.Textarea)
```

# 4. Django ModelForm

### Form
- 사용자 입력 데이터를 DB에 저장하지 않을 때, 로그인

### ModelForm
- 사용자 입력 데이터를 DB에 저장해야 할 때, 회원가입

### ModelForm class 선언

``` python
# articles/forms.py

from django import forms
from .models import Ariticle

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```

### Meta class
- ModelForm의 정보를 작성하는 곳

### fields 및 exclude 속성
- exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음

### ModelForm을 적용한 create 로직

``` python

from .forms import ArticleForm

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)   
```

### is_valid()
- 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환

### ModelForm을 적용한 edit 로직

``` python
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    form = ArticleForm(request.POST, instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

### ModelForm을 적용한 update 로직

``` python
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    form = ArticleForm(instance=article)
    if form.is_valid()
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }

    return render(request, 'articles/edit.html', context)
```

### save()
- 데이터베이스 객체를 만들고 저장
- 키워드 인자 instance 여부를 통해 생성할지, 수정할지를 결정

# 99. 참고

### Widget 응용

``` python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목', 
        widget = forms.TextInput(
            attrs = {
                'class': 'my-title',
                'placeholder': '제목을 입력해주세요.'
            }
        )
    )
    
    content = forms.CharField(
        label = '내용', 
        widget = forms.Textarea(
            attrs = {
                'class': 'my-content',
                'placeholder': '내용을 입력해주세요.',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages = {'required': '내용을 입력해주세요.'},
    )
    
    # ModelForm의 정보를 작성하는 곳
    class Meta:
        model = Article
        # fields = ('title',)
        # exclude = ('title',)
        fields = '__all__'
```

### Meta class
- 클래스 안에 클래스, 파이썬에서는 Inner class or Nested class
- 파이썬의 문법적 개념으로 접근하지 말 것
- 단순히 모델 정보를 Meta라는 이름의 내부 클래스로 작성하도록 ModelForm의 설계가 이렇게 되어있을 뿐
- `ModelForm의 역할과 사용법을 숙지하는데 집중`할 것

