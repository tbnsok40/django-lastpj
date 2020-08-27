from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from django.utils import timezone 
from .forms import MemoForm

def index(request):
    index = Memo.objects
    return render(request, 'index.html', {'index': index})
def new(request):
    return render(request, 'new.html')

# Create    
def create(request):
    memo = Memo()
    memo.title = request.GET['title']
    memo.content = request.GET['content']
    memo.pub_date = timezone.datetime.now()
    memo.save()
    return redirect('/memo/'+str(memo.id))


def memoform(request):
    if request.method == 'POST': # POST요청이 들어왔을 때
        form = MemoForm(request.POST) # 요청을 통해 들어온 내용을 form에 담는다(아직 저장X)
        if form.is_valid():
            memo = form.save(commit=False) 
            # 아직 pub_date를 담아두지 않아서 담아만 둔 상태save(commit=False)
            memo.pub_date = timezone.now()
            memo.save()
            return redirect('index') # 모델만 쓸 때와 비슷한 형식 (다만, memo.id만 넘겨주지 않았다.)
    else: # 위의 두 if문 중에 어디에 속하는지 잘 파악할 것
        form = MemoForm()
        return render(request, 'new.html',{'form':form})

# Read
def detail(request, memo_id):
    context = get_object_or_404(Memo, pk = memo_id)
    return render(request, 'detail.html', {'context' : context})

# Delete
def delete(request, memo_id):
    memo = get_object_or_404(Memo, pk = memo_id)
    memo.delete()
    return redirect('index')

# Update
def edit(request, memo_id): # 복습자료에는 ,memo_id 없었음
    memo = get_object_or_404(Memo, pk = memo_id)
    return render(request, 'edit.html',{'memo':memo})
    # 복습자료에는 url => memo/edit.html 
# def update(request, memo_id):
#     memo = get_object_or_404(Memo ,pk = memo_id)
#     memo.title = request.GET.get('title')
#     memo.content = request.GET.get('content')
#     memo.pub_date = timezone.datetime.now()
#     memo.save()
#     return redirect('/memo/'+ str(memo.id))

# modelform을 이용한 update
def update(request, post_id):
	memo = get_object_or_404(Memo, pk = post_id)
	if request.method == 'POST':
		form = MemoForm(request.POST, instance=memo)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('detail', memo_id=memo.pk) # 수정한 글의 상세 페이지로 돌아가겠습니다. 
	else:
		form = MemoForm(instance=memo) # memo 객체에 이미 저장돼있는 것들을 form에 띄워줍니다. 
		return render(request, 'edit.html', {'form': form})


