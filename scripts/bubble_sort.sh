#set -x

# Reverses the order of the array given as input.
# Example:
# > invert 1 2 3
#   3 2 1
invert() {
    local inverted
    for i in $@; do
        inverted=($i ${inverted[@]})
    done
    
    echo ${inverted[@]}
}

numbers=$(invert $@)

echo ${numbers[@]}

set +x
