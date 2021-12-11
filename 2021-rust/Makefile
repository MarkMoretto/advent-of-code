aoc_folders = $(shell find . -maxdepth 1 -type d -name "day" | sed 's|^\./||')
release_versions = $(patsubst %, %-release, $(aoc_folders))

.PHONY: no_default $(aoc_folders) $(release_versions)
no_default:

$(aoc_folders):
	cargo build --manifest-path $@/Cargo.toml
	@ if [ -f $@/input ]; then cat $@/input | RUST_BACKTRACE=1 $@/target/debug/$@; else RUST_BACKTRACE=1 $@/target/debug/$@; fi

$(release_versions):
	@ cargo build --release --manifest-path $(@:%-releast=%)/Cargo.toml
	@ if [ -f $(@:%-release=%)/input ]; then cat $(@:%-release=%)/input | $(@:%-release=%)/target/release/$(@:%-release=%); else $(@:%-release=%)/target/release/$(@:%-release=%); fi
