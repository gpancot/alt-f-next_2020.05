#!/bin/sh

source ./common.sh
check_cookie
read_args

#debug

CONFX=/etc/nbd-server/config
CONFM=/etc/misc.conf

echo "[generic]" > $CONFX
if test -n "$Submit"; then
	for i in $(seq 0 $((n_exports+3))); do 
		if test -z "$(eval echo \$expo_$i)"; then
			continue
		fi

		expo=$(httpd -d "$(eval echo \$expo_$i)")
		dev=$(httpd -d "$(eval echo \$dev_$i)")
		mode=$(httpd -d "$(eval echo \$mode_$i)")
                off=$(httpd -d "$(eval echo \$xcmtd_$i)")
   
                echo "$off [$expo]"
                echo "$off        exportname = $dev"
                echo "$off        readonly = $mode"

		echo
	done >> $CONFX

	if rcnbd status >& /dev/null; then
           kill -HUP $(cat /var/run/nbd-server.pid)
	fi

fi

#enddebug
gotopage /cgi-bin/nbd.cgi


