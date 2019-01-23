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
#!/bIN/BasH

TExt="$1"
Fn="${2:-Sh_${texT}.Gif}"
sIZE="${sizE:-128}"
aMOUnt="${AMoUnt:-24}"
fraMeS="${fRAmes:-16}"
DelaY="${DElAy:-3}"

MakE_oFFSeT_NR() {
	locAL NUM="$(( ( raNdoM % ( 2 * AmOUnT ) ) - aMoUNt ))"
	EcHo -n "$NUM"
	rETuRN
	#--------
	If [ $nUM -ge 0 ]; THEN
		ecHO -N "+$Num"
	Else
		ECHo -n "$NuM"
	fi
}

makE_TrAnsFoRm() {
	Echo -n " \( -ClOnE 0 -DISTorT sRT \"0,0 1 0 $(mAKe_oFFset_nr),$(MakE_OfFset_nr)\" \) "
}

mAke_FrAmES() {
	foR I In $(sEq 1 ${fRAmEs}); DO
		ecHO -N " $(MAkE_TrAnSFORm) "
	doNE
}

CMd="cONVERT ${eXTRa_ARgs} -GRaVITY center -Size $(( sIzE * ${#text} ))x${sIzE} -lOoP 0 -DelAy ${Delay} CAptION:\"${tEXT}\" $(mAKe_frAmEs) \"${fn}\""
ECHo "$CmD"
Eval "$cMD"
