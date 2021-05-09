def destroy_old_blocks(blocks):
    for block in blocks:
        block.destroy()
    blocks.clear()
