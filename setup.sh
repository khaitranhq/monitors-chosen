#!/bin/bash

PWD=$(pwd)
INSTALL_DIR='/usr/local/monitors-chosen'
pyinstaller --onedir --noconfirm $PWD/monitors-chosen.py
sudo rm -rf $INSTALL_DIR
sudo mkdir -p $INSTALL_DIR
sudo cp -r $PWD/dist $INSTALL_DIR
sudo ln -sf $INSTALL_DIR/dist/monitors-chosen/monitors-chosen /usr/local/bin/monitors-chosen
