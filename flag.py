import tensorflow as tf

tf.app.flags.DEFINE_float("learning_rate", 0.0003, "Learning rate.")
tf.app.flags.DEFINE_float("learning_rate_decay_factor", 0.95, "Learning rate decays by this much.")
tf.app.flags.DEFINE_float("max_gradient_norm", 10.0, "Clip gradients to this norm.")
tf.app.flags.DEFINE_float("dropout", 0.15, "Fraction of units randomly dropped on non-recurrent connections.")
tf.app.flags.DEFINE_integer("batch_size", 128, "Batch size to use during training.")
tf.app.flags.DEFINE_integer("epochs", 40, "Number of epochs to train.")
tf.app.flags.DEFINE_integer("size", 400, "Size of each model layer.")
tf.app.flags.DEFINE_integer("num_layers", 3, "Number of layers in the model.")
tf.app.flags.DEFINE_integer("max_seq_len", 100, "Maximum sequence length.")
tf.app.flags.DEFINE_string("data_dir", "/tmp", "Data directory")
tf.app.flags.DEFINE_string("train_dir", "/tmp", "Training directory.")
tf.app.flags.DEFINE_string("voc_dir", '/tmp', "The vocabulary folder")
tf.app.flags.DEFINE_string("out_dir", "/tmp", "Output directory")
tf.app.flags.DEFINE_string("tokenizer", "CHAR", "BPE / CHAR / WORD.")
tf.app.flags.DEFINE_string("optimizer", "adam", "adam / sgd")
tf.app.flags.DEFINE_integer("print_every", 1, "How many iterations to do per print.")
tf.app.flags.DEFINE_integer("beam_size", 128, "Size of beam.")
tf.app.flags.DEFINE_integer("max_wit", 50, "number of witnesses.")
tf.app.flags.DEFINE_string("decode", 'single', "single/weight/average/flat")
FLAGS = tf.app.flags.FLAGS
