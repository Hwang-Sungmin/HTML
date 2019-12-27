#### DOM과 이벤트 처리

**문서 객체 모델 ( DOM : Document Object Model )**

- HTML 문서의 계층적인 구조를 tree로 표현
- 자바스크립트에서는 HTML 문서와 웹 브라우저를 객체로 간주하여 처리 (웹 -> BOM)



연습하기

##### html요소 찾기

````javascript
var x = document.getElementById("main"); #문서 안에서 id가 main인 요소를 찾아서 반환
alert(document.getElementById("main").innerHTML); # alert으로 main의 내용을 출력
````

````javascript
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>DOM 연습</title>
</head>
    <script>
        function process(){
            var obj = document.getElementById("target");
      	              // document.myform.text1 (두번째 방법)
            alert(obj.value);
        }
    </script>
<body>
    <form name="myform">
        <input type="text" id="target" name="text1">
        <input type="submit" value="제출" onclick="process()">
    </form>

</body>
</html>
````



###  jQuery

- 문장구조
  - $( selector ).action()
    - selector 가 ".aaa" - class name이 aaa인 요소, "#.aaa" id가 aaa인 요소

````javascript
$(documnet).ready(function(){
  	//DOM이 로딩되어서 준비되면 작업을 시작한다.
  	//구체적으로 jQuery 메서드를 호출한다
});
````

- jQuery를 이용한 DOM 변경

  - 요소의 내용을 가져오거나 변경 - text() , html()
  - 요소의 속성을 가져오거나 변경 - attr()
  - 요소의 스타일 속성을 가져오거나 변경 - css()
  - 요소를 추가하거나 삭제 - append() , remove()

  ````javascript
  # 요소의 콘텐츠 가져오기
  $("#target).text(); //id가 target인 요소의 텍스트를 가져온다

  #요소의 속성 가져오기
  $(selector).attr(attributeName); 
  ````



###  Ajax (Asynchronous JavaScript and XML)

- 서버와 데이터를 교환하는 기술 
- 클라이언트가 서버와 적은 양의 데이터를 교환하여 비동기적으로 HTML을 업데이트

````javascript
# get()
$.get(URL, callback);

# 서버로 부터 파일을 가져오는 코드
$("button").click(function(){
  $.get("test.jsp") , function(data, status){
  	alert("데이터: " + data + "상태 :" +status);
  });	
});

# post()
$.post(URL, data, callback)

# load()
$.load(URL, data, callack)
````



###  JSON ( JavaScript Object Notation )

