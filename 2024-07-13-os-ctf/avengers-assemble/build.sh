#!/usr/bin/env bash

SOURCE_FILE="code.asm"
OUTPUT_FILE="code"
CC="gcc"
ASM="nasm"
CFLAGS="-m32 -no-pie"
ASMFLAGS="-f elf32"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' 

log() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

build() {
    log "Assembling ${SOURCE_FILE}..."
    if ! $ASM $ASMFLAGS $SOURCE_FILE -o "${SOURCE_FILE%.asm}.o"; then
        error "Assembly failed"
        return 1
    fi

    log "Linking..."
    if ! $CC $CFLAGS "${SOURCE_FILE%.asm}.o" -o $OUTPUT_FILE; then
        error "Linking failed"
        return 1
    fi

    rm ./*.o

    log "Build complete. Executable: $OUTPUT_FILE"
}

clean() {
    log "Cleaning..."
    rm -f $OUTPUT_FILE "${SOURCE_FILE%.asm}.o"
    log "Clean complete"
}

run() {
    if [ ! -f $OUTPUT_FILE ]; then
        warn "Executable '$OUTPUT_FILE' not found. Building first..."
        if ! build; then
            error "Build failed. Cannot run."
            return 1
        fi
    fi
    log "Running $OUTPUT_FILE..."
    ./$OUTPUT_FILE
}

check_dependencies() {
    for cmd in $CC $ASM; do
        if ! command -v $cmd &> /dev/null; then
            error "$cmd is not installed. Please install it to continue."
            exit 1
        fi
    done
}

check_dependencies

case "$1" in
    build)
        build
        ;;
    clean)
        clean
        ;;
    run)
        run
        ;;
    all)
        clean && build && run
        ;;
    *)
        echo "Usage: $0 {build|clean|run|all}"
        exit 1
        ;;
esac
