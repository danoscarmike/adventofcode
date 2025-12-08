from enum import Enum
import sys

from collections import defaultdict

sys.path.append("../utilities")

from utilities.input import read_file_to_string


class BlockType(Enum):
    FILE = 0
    FREE = 1


class Block:
    def __init__(self, type: BlockType, size: int, block_id: int, file_id: int = None):
        self.type = type
        self.size = size
        self.start_id = block_id
        self.file_id = file_id
    
    def __repr__(self):
        rep_str = f"{self.file_id if self.type == BlockType.FILE else "."}" * self.size
        return f'{rep_str} ({self.type})'
        # return f"{self.type} - {self.size} - {self.start_id} - {self.file_id}"


def print_disk_map(file_blocks: list):
    repr_str = ''
    for block in file_blocks:
        repr_str = repr_str + ''.join(str(block.file_id) if block.file_id is not None else '.' for _ in range(block.size))
    print(repr_str)


def map_to_disk(disk_map: str) -> tuple[list]:
    file_blocks, free_block_indices = [], []

    block_id = 0

    for map_id, block_size in enumerate(disk_map):
        if map_id % 2 == 0:
            # this is a file block
            file_id = map_id // 2
            for _ in range(int(block_size)):
                file_blocks.append(file_id)
                block_id += 1
        else:
            # this is a free block
            for _ in range(int(block_size)):
                file_blocks.append(None)
                free_block_indices.append(block_id)
                block_id += 1

    return file_blocks, free_block_indices


def map_to_disk_v2(disk_map: str) -> list:
    file_block_list = []

    block_id = 0

    for map_id, block_size in enumerate(disk_map):
        if map_id % 2 == 0:
            # this is a file block
            file_id = map_id // 2
            file_block_list.append(Block(BlockType.FILE, int(block_size), block_id, file_id))
            block_id += int(block_size)
        else:
            # this is a free block
            file_block_list.append(Block(BlockType.FREE, int(block_size), block_id))
            block_id += int(block_size)
    
    return file_block_list


def calculate_checksum(file_blocks: list) -> int:
    checksum = 0
    for j in range(len(file_blocks)):
        if file_blocks[j] is not None:
            checksum += j * file_blocks[j]
    return checksum


def calculate_checksum_v2(file_blocks: list) -> int:
    checksum = 0
    for block in file_blocks:
        if block.type == BlockType.FILE:
            for i in range(block.size):
                checksum += block.file_id * (block.start_id + i)
    return checksum


def part_one(disk_map: str) -> int:
    file_blocks, free_block_indices = map_to_disk(disk_map)

    for i in range(len(file_blocks) - 1, -1, -1):
        if i < free_block_indices[0]:
            break
        if file_blocks[i] is not None:
            if len(free_block_indices) == 0:
                continue
            file_blocks[free_block_indices.pop(0)] = file_blocks[i]
            file_blocks[i] = None
            free_block_indices.append(i)
            free_block_indices.sort()

    return calculate_checksum(file_blocks)


def part_two(disk_map: str) -> int:
    file_blocks = map_to_disk_v2(disk_map)
    base_map = file_blocks.copy()
    print_disk_map(file_blocks)

    for i, block in enumerate(reversed(base_map)):
        print(f"Checking free space for file #{block.file_id}")
        if block.type == BlockType.FILE:
            for j, target_block in enumerate(file_blocks):
                if target_block.type == BlockType.FREE and target_block.size >= block.size:
                    free_size = target_block.size
                    file_blocks[j] = Block(BlockType.FILE, block.size, target_block.start_id, block.file_id)
                    if free_size - block.size > 0:
                        file_blocks.insert(j+1, Block(BlockType.FREE, free_size - block.size, j + free_size - block.size))
                    file_blocks[-1-i] = Block(BlockType.FREE, block.size, block.start_id)
                    print_disk_map(file_blocks)
                    break

    print_disk_map(file_blocks)
    
    return calculate_checksum_v2(file_blocks)


if __name__ == "__main__":
    disk_map = read_file_to_string(sys.argv[1])
    print(part_one(disk_map))
    print(part_two(disk_map))
