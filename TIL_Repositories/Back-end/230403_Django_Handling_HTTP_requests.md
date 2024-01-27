# 11. Django - Handling_HTTP_requests

## 학습 목표

> HTTP requests methods를 사용해 효율적인 view 함수 구조를 작성할 수 있다.

# 1. 개요

### HTTP requests 처리에 따른 view 함수 구조 변화

### new & create view 함수간 공통점과 차이점
- 공통점: "데이터 생성 로직을 구현하기 위함"
- 차이점: "new는 GET method 요청만을, create는 POST method 요청만을 처리"

# 2. view 함수의 변화

``` python
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
```
