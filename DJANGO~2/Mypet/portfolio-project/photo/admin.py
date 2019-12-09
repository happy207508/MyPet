from django.contrib import admin

from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    # PhotoAdmin 클래스에는 관리자 사이트에서 보이는 목록 화면을 커스터마이징 할 수 있는 옵션을 설정
    list_display = ['id','author','created','updated']
    # 목록에 보일 필드를 설정한다. 모델의 필드를 선택하거나 별도 함수를 만들어 필드처럼 등록할 수 있다.
    raw_id_fields = ['author']
    # ForeignKey 필드의 경우 연결된 모델의 객체 목록을 출력하고 선택해야 하는 목록이 너무 길 경우 불편해진다.
    # 이런 경우 raw_id_fields로 설정하면 값을 써 넣는 형태로 바뀌고 검색 기능을 사용해 선택할 수 있게 된다.
    list_filter = ['created','updated','author']
    # 필터 기능을 사용할 필드를 선택합니다. 장고가 적절하게 필터 범위를 출력해준다.
    search_fields = ['text','created']
    # 검색 기능을 통해 검색할 필드를 선택한다. ForeignKey 필드는 설정할 수 없다. ex) author
    ordering = ['-updated','-created']
    # 모델의 기본 정렬값이 아닌 관리자 사이트에서 기본으로 사용할 정렬값을 설정한다.
    # -updated, -created = 내림차순

admin.site.register(Photo, PhotoAdmin)