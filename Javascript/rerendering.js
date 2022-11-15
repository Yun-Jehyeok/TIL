// 문제 1
// 본인 댓글 수정을 위해 텍스트 필드를 인풋 필드로 바꿔야 했다.
// users [ user: { isEditMode: boolean, ... }, ...]의 isEditMode를 바꿔가며 화면을 바꿔줬는데 lwc 문제인건지 js 문제인건지 리렌더링이 되지 않는 문제 발생
// 변수의 depth가 깊은건지, DOM에서의 노드 depth가 깊은건지... 이유는 찾지 못함

// 제대로 된 해결방법은 못 찾았고 (애초에 왜 안되는지도 모르겠고) 기간 내에 수정은 해야되기 때문에 편법 사용

// 편법 쓰기 전 코드
// html
{
  item.isEditMode ? (
    <div data-key={item.id} onclick={deleteReview}>
      삭제
    </div>
  ) : (
    <div>
      <div
        data-key={item.id}
        data-content={item.content}
        onclick={changeToEdit}
      >
        수정
      </div>
      <div data-key={item.id} onclick={deleteReview}>
        삭제
      </div>
    </div>
  );
}

// js
const changeMode = (data) => {
  this.reviews = this.reviews.map((item) => {
    if (item.id === data) {
      item.isEditMode = !item.isEditMode;
    }

    return item;
  });
};

// 편법 사용 후 코드
// 아무 의미도 공간도 차지 하지 않는 span 공간을 edit 모드일 때만 출력
// html
{
  isEditMode ? <span></span> : "";
}
{
  item.isEditMode ? (
    <div data-key={item.id} onclick={deleteReview}>
      삭제
    </div>
  ) : (
    <div>
      <div
        data-key={item.id}
        data-content={item.content}
        onclick={changeToEdit}
      >
        수정
      </div>
      <div data-key={item.id} onclick={deleteReview}>
        삭제
      </div>
    </div>
  );
}

// js에서 span 태그를 보여줄 isEditMode 변수를 하나 추가해 변경
// js
changeMode = (data) => {
  this.isEditMode = !this.isEditMode;
  this.reviews = this.reviews.map((item) => {
    if (item.id === data) {
      item.isEditMode = !item.isEditMode;
    }

    return item;
  });
};
