import json
import os

from utils import read

class Config:
  def __init__(self, conf_path):
    conf = self.load_conf(conf_path)
    self.batch_size = conf['model']['batch_size']
    self.bug_dir = conf['bug_dir']
    self.data_dir = conf['data_dir']
    self.emb_size = conf['model']['emb_size']
    self.eng_name = conf['eng_name']
    self.eng_path = conf['eng_path']
    self.gpu = conf['gpu']
    self.epoch = conf['model']['epoch']
    self.gamma = conf['model']['gamma']
    self.lr = conf['model']['lr']
    self.max_ins = conf['max_ins']
    self.model_path = conf['model_path']
    self.momentum = conf['model']['momentum']
    self.split_size = conf['model']['split_size']
    self.test_frac = conf['model']['test_frac']
    self.type_loss_weight = conf['model']['type_loss_weight']
    self.weight_decay = conf['model']['weight_decay']
    self.num_gpu = conf['num_gpu']
    self.num_proc = conf['num_proc']
    self.opt = conf['opt']
    self.run_mode = conf['run_mode']
    self.seed_dir = conf['seed_dir']
    self.timeout = conf['timeout']
    self.top_k = conf['top_k']

    self.ast_dir = os.path.join(self.data_dir, 'ast')
    self.log_dir = os.path.join(self.data_dir, 'log')

  def load_conf(self, conf_path):
    conf = read(conf_path, 'r')
    dec = json.JSONDecoder()
    conf = dec.decode(conf)
    return conf
