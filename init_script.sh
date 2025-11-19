echo"A script to create, activate and install requirements"
echo"........"

virtualenv venv

echo"creation of virtualenv done....."
echo"Activation my env"
source venv/bin/activate

echo"........"
echo"install requitement.txt"
pip install -r requirement.txt

sleep(2)
echo"install done"
echo"Creation Acitvation and installation done"
