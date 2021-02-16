import os
import pickle
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--trees-dir",
    type=str,
    default="~/Desktop/NetworksProject/neurocuts/dump_trees",
    help="compute statistics for trees in this directory")



def collect_stats(dir_path):
	directory_in_str = dir_path
	directory = os.fsencode(directory_in_str)

	bytes_per_rule_sum = 0
	memory_access_sum = 0
	num_leaf_node_sum = 0
	num_nonleaf_node_sum = 0
	num_node_sum = 0
	num_of_trees = 0

	for file in os.listdir(directory):
		filename = dir_path + "/" + os.fsdecode(file)
		with open(filename, "rb") as f:
			tree = pickle.load(f)
			cur_tree_stats = tree.compute_result()

			bytes_per_rule_sum += cur_tree_stats["bytes_per_rule"]
			memory_access_sum += cur_tree_stats["memory_access"]
			num_leaf_node_sum += cur_tree_stats["num_leaf_node"]
			num_nonleaf_node_sum += cur_tree_stats["num_nonleaf_node"]
			num_node_sum += cur_tree_stats["num_node"]
			num_of_trees += 1

	return bytes_per_rule_sum, memory_access_sum, num_leaf_node_sum, num_nonleaf_node_sum, num_node_sum, num_of_trees


def print_averages(stats):
	bytes_per_rule_avg = stats[0] / stats[5]
	print("bytes_per_rule_avg:", bytes_per_rule_avg)

	memory_access_avg = stats[1] / stats [5]
	print("memory_access_avg:", memory_access_avg)

	num_leaf_node_avg = stats[2] / stats [5]
	print("num_leaf_node_avg:", num_leaf_node_avg)

	num_nonleaf_node_avg = stats[3] / stats [5]
	print("num_nonleaf_node_avg:", num_nonleaf_node_avg)

	num_node_avg = stats[4] / stats [5]
	print("num_node_avg:", num_node_avg)




def main():
	args = parser.parse_args()
	dir_path = "./result_trees/" + args.trees_dir

	stats = collect_stats(dir_path)
	print("num_of_trees", stats[5])
	print_averages(stats)



if __name__ == "__main__":
	main()
