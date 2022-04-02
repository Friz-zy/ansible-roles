#!/bin/bash
# https://borgbackup.readthedocs.io/en/latest/usage/prune.html

args="$@"
ARCHIVE=$(echo $args | grep -Po "\s\S*::\S*\s")

while :
do
    case "$1" in
      -h | --help)
          borg prune --help
          exit 0
          ;;
      --) # End of all options
          shift
          break
          ;;
      *)  # No more options
          break
          ;;
    esac
done

# less io and cpu priority
ionice -c3 -p$$
renice -n 10 $$
# ulimit -m 1024000 memory limit 1gb

info() { printf "\n%s %s\n\n" "$( date '+%Y-%m-%d %H:%M' )" "$*" >&2; }
trap "echo $( date '+%Y-%m-%d %H:%M' ) Pruning of $BORG_REPO$ARCHIVE interrupted >&2; exit 2;" INT TERM

info "Pruning $BORG_REPO$ARCHIVE"
borg prune $args
exit=$?
if [ ${exit} -eq 0 ];
then
    info "Pruning of $BORG_REPO$ARCHIVE finished"
elif [ ${exit} -eq 1 ];
then
    info "Pruning of $BORG_REPO$ARCHIVE finished with a warning"
elif [ ${exit} -gt 1 ];
then
    info "Pruning of $BORG_REPO$ARCHIVE finished with an error"
fi
