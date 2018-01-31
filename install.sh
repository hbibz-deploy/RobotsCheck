echo "------------------------------"
echo "- Running Installation"
pip install -r requirements.txt || echo "install pip first and rerun"
cp -R . /opt/robot && cd /opt/robot
export PATH=$PATH:`pwd` && echo "added to your PATH"