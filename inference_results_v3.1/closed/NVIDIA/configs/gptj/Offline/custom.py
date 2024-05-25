# Generated file by scripts/custom_systems/add_custom_system.py
# Contains configs for all custom systems in code/common/systems/custom_list.py

from . import *


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99, PowerSetting.MaxP)
class OCEJON(OfflineGPUBaseConfig):
    system = KnownSystem.ocejon
    # Applicable fields for this benchmark are listed below. Not all of these are necessary, and some may be defined in the BaseConfig already and inherited.
    # Please see NVIDIA's submission config files for example values and which fields to keep.
    # Required fields (Must be set or inherited to run):
    gpu_batch_size: int = 1
    #input_dtype: str = ''
    #input_format: str = ''
    precision: str = 'fp16'
    #tensor_path: str = ''

    # Optional fields:
    #active_sms: int = 0
    #buffer_manager_thread_count: int = 0
    #cache_file: str = ''
    #coalesced_tensor: bool = False
    enable_sort: bool = False
    gpu_copy_streams: int = 1
    gpu_inference_streams: int = 1
    #instance_group_count: int = 0
    #model_path: str = ''
    num_sort_segments: int = 2
    #numa_config: str = ''
    offline_expected_qps: float = 1000.0
    #performance_sample_count_override: int = 0
    #preferred_batch_size: str = ''
    #request_timeout_usec: int = 0
    #run_infer_on_copy_streams: bool = False
    tensor_parallelism: int = 1
    #use_fp8: bool = False
    #use_graphs: bool = False
    #use_jemalloc: bool = False
    #use_spin_wait: bool = False
    #verbose_glog: int = 0
    #workspace_size: int = 0


@ConfigRegistry.register(HarnessType.Custom, AccuracyTarget.k_99_9, PowerSetting.MaxP)
class OCEJON_HighAccuracy(OCEJON):
    pass



