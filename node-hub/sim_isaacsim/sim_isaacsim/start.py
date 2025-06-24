from omni.isaac.kit import SimulationApp

simulation_app = SimulationApp({
    "headless": False,
})

import hydra
from omegaconf import DictConfig

from src.utils import debug, set_seed


@hydra.main(config_path="./configs", config_name="stack_cube_dp_franka", version_base="1.3.2")
def main(cfg: DictConfig):
    if "seed" in cfg.keys():
        set_seed(cfg.seed)

    task_cfg = cfg.task
    task = hydra.utils.instantiate(task_cfg)

    print(f"Task '{type(task).__name__}' initialized.")

    task.run(simulation_app)


if __name__ == "__main__":
    # debug()
    main()
