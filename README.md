# Table_ocr for NIA-solution_for_social_issue
***
*원본 소스: <https://github.com/eihli/image-table-ocr>
***
## Input_data
>img_file = './0001.png'
- 표 정보를 담은 단일한 이미지 파일(*.png) 경로
***
## Output_data
- 표가 있는 이미지 파일(.png)에서 표를 각 셀을 추출하여 
```python
<table>\인식된표의정보\</table> 코드 반환
```  
- 표 정보 전체에 대한 인식 불가시 return: None
- 표 내부의 일부 셀에 대한 텍스트정보 인식 불가시: NaN
>출력 예)<table><tr><td>Time (drops Of water)</td><td>Distance (cm)</td></tr><tr><td>1</td><td>10,11,9</td></tr><tr><td>2</td><td>29, 31, 30</td></tr><tr><td>3</td><td>59, 58, 61</td></tr><tr><td>NaN</td><td>102, 100, 98</td></tr><tr><td>5</td><td>122, 125, 127</td></tr></table>
***
## 성능 검증 모듈 evaluation 추가
'''from image2table import img2table
img2table.evaluation(reader ,test_dataset_dir='', ouput_dir='')
	#test_dataset_dir = 'str' -> 성능 검증에 사용될 데이터의 디렉토리
	#output_dir = 'str' 	      -> 파일 출력 경로
'''
##성능 검증을 위한 test_dataset_dir(예: evalData)의 구성
```evalData
├── class
│   ├── 0.png
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   └── 4.png
├── name.txt
└── gt.txt
``` 
***

  ## 변경사항
 * 21년 12월 14일
   * convert, evaluation 파라미터 수정

 * 21년 12월 3일
  * 성능 검증을 위한 evaluation 메서드 및 검증 데이터 추가

 * 21년 10월 13일
   * convert 메서드에 출력형식 변경을 위한 파라미터 추가(output='html' or 'text'  / default: output='html')

 * 21년 10월 5일
   * 셀 내부 텍스트 데이터 처리를 방식을 문단 단위에서 줄단위로 변경(paragraph=False)

 * 21년 10월 1일
   * 표 인식 성능 개선(borderless 표모델 인식 추가)


  * 21년 8월 27일
    * textOCR과 OCR모델 통합
       
        * 각 메서드 사용시 지정된 reader 전달인자를 지정해 줄 것
        * 각 메서드의 custom_model 파라미터 제거
        ```python
        from image2table import img2table
        img2table.convert(reader, img_file='')
        ```
    * 라이브러리 의존성 개선
    

  * 21년 8월 24일
    * 동서대 모듈과의 통합을 위해 torch==1.9.0, torchVision==0.10.0으로 라이브러리가 변경
    * torch, torchvision을 제외한 나머지 라이브러리는 버전을 고정시키지 않고, 최소버전 이상 호환되게 변경

  * 21년 8월 20일
     * bugfix: TextOCR의 커스텀 모델 사용 가능
     * Ubuntu 개발 환경에 대한 패키지 사용성 개선
    
  * 21년 8월 17일    
    * 표가 있는 이미지 파일(.png)에서 표를 각 셀을 추출하여 html \<table>\</table> 코드로 터미널에 출력
    * 기존 테이블 이미지 및 셀 이미지, 텍스트 파일, csv 파일, html 파일 저장되지 않게 코드 수정
    * 각 모듈에 넘겨줄때 numpy array형태로 넘겨 줌
    
* 21년 8월 9일
    * OCR 라이브러리 변경 완료(Tesseract -> NIA_textOCR(easyOCR 기반)
    * NIA_textOCR의 커스텀 모델 사용 가능
    * 패키지 사용성 수정(image2table/img2text.py)
* 21년 7월 23일
    * 이미지 파일(.png)에서 표(테이블)이 있는 이미지 파일에서 표만 추출하여 폴더 생성 후 이미지 파일(.png)로 저장
    * 표 이미지 파일(.png)에서 전처리 후 각 셀을 추출, 폴더 생성 후 이미지 파일(.png)로 저장
    * 셀 이미지 파일을 OCR하기 편하게 전처리 작업 후 폴더 생성 이미지 파일로 저장
    * 전처리 된 셀 이미지 파일(.png)을 OCR 작업을 거친 후 각 셀 이미지 파일(.png)에 대한 텍스트 파일(.gt.txt) 생성 및 전체 csv 파일, html 파일 생성
    * html table 코드 출력
  
##설치
- python 개발환경은 3.8.5입니다.
```python
pip install git+https://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@github.com/SANGJUN12-KIM/NIA-TableOCR.git
```
## 사용법
```python
 from image2table import img2table
 img2table.convert(reader, img_file='')
	# img_file = 'str'              -> 정보를 추출할 표 이미지가 저장된 경로
 ```
```python
 from image2table import img2table
 img2table.evaluation(reader, test_dataset_dir,output_dir)
	#test_dataset_dir = 'str' -> 성능 검증에 사용될 데이터의 디렉토리
	#output_dir = 'str' 	      -> 파일 출력 경로
 ```

