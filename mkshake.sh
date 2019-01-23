#!/bin/bash

TEXT="$1"
FN="${2:-sh_${TEXT}.gif}"
SIZE="${SIZE:-128}"
AMOUNT="${AMOUNT:-24}"
FRAMES="${FRAMES:-16}"
DELAY="${DELAY:-3}"

make_offset_nr() {
	local NUM="$(( ( RANDOM % ( 2 * AMOUNT ) ) - AMOUNT ))"
	echo -n "$NUM"
	return
	#--------
	if [ $NUM -ge 0 ]; then
		echo -n "+$NUM"
	else
		echo -n "$NUM"
	fi
}

make_transform() {
	echo -n " \( -clone 0 -distort SRT \"0,0 1 0 $(make_offset_nr),$(make_offset_nr)\" \) "
}

make_frames() {
	for i in $(seq 1 ${FRAMES}); do
		echo -n " $(make_transform) "
	done
}

CMD="convert ${EXTRA_ARGS} -gravity Center -size $(( SIZE * ${#TEXT} ))x${SIZE} -loop 0 -delay ${DELAY} caption:\"${TEXT}\" $(make_frames) \"${FN}\""
echo "$CMD"
eval "$CMD"
