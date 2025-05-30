# xkeysnail config for different devices

> [!WARNING]
> xkeysnail is not maintained anymore, moved to using [xremap](https://github.com/xremap/xremap)

List of config files I use for different device setups.

---

#### [Run xkeysnail without sudo](https://github.com/mooz/xkeysnail/issues/64#issuecomment-600380800)

```
$ sudo groupadd -f uinput
$ sudo gpasswd -a $USER uinput
$ cat <<EOF | sudo tee /etc/udev/rules.d/70-xkeysnail.rules
KERNEL=="uinput", GROUP="uinput", MODE="0660", OPTIONS+="static_node=uinput"
KERNEL=="event[0-9]*", GROUP="uinput", MODE="0660"
EOF
```

#### Run in startup

Do `which xkeysnail` to know the location of xkeysnail then add the following in your Application Autostart (or anything similar in the DE you are using)

```
/usr/bin/xkeysnail /home/YOUR_USERNAME/.xkeysnail-config/SELECT_CONFIG.py --devices /dev/input/event# /dev/input/event# --quiet
```

---

#### Run in background

```
xkeysnail .xkeysnail-config/SELECT_CONFIG.py --quiet </dev/null &>/dev/null &
```
