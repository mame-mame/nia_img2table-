from setuptools import setup, find_packages

setup(
    name='niaimage2table',
    version='1.0',
    description='Extract text from tables in images.',
    author='Bae Yong Bin',
    author_email='mame-mame@kakao.com',
    url='',
    download_url='',
    install_requires=['numpy>=1.19.5', 'torch==1.9.0', 'torchvision==0.10.0', 'opencv-python>=4.5.2.52', 'easyocr','requests'],
    packages=find_packages(),
    keywords=['Extract_text', 'table_ocr', 'easyOCR'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)