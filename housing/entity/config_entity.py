from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",["downlod_datset_url","tgz_owuload_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidataionConfig =namedtuple("DataValidataionConfig",["scema_file_path"])

DataTransfoarmationConfig = namedtuple("DataTransfoarmationConfig",["add_bedroom_per_home",
                                                                    "transformed_train_dir",
                                                                    "transformed_test_dir",
                                                                    "preprocessed_object_file_path"])
ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy"])

ModelEvaluationConfig =  namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])

ModelPushConfig = namedtuple("ModelPushConfig",["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])




