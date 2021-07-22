#/bin/bash

if [ "$1" == "--list" ]; then
cat<<EOF
{
  "bash_hosts": {
    "hosts": [
      "192.168.2.25",
      "192.168.2.35"
    ],
    "vars": {
      "script_var": "test-value"
    }
  },
  "_meta": {
    "hostvars": {
      "squid.galaxy": {
        "squid_script_var": "test-value"
      }
    }
  }
}
EOF
elif [ "$1" == "--host" ]; then
  echo '{"_meta": {hostvars": {}}}'
else
  echo "{ }"
fi
