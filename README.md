nnocada建venv时不好用，如下方式

在项目路径下新建虚拟环境文件夹: venv

pyvenv --without-pip venv

source venv/bin/activate

curl https://bootstrap.pypa.io/get-pip.py | python

deactivate

source venv/bin/activate

pip install flask
或者 pip install -e .

Flask 启动

export FLASK_APP=flaskr

export FLASK_ENV=development

flask run
