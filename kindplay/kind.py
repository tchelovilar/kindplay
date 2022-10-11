import stat
import tempfile
import yaml
import os

from tools import run_command


def run_scripts(script_list, base_path):
    script_header = "#!/bin/bash\n"
    env = os.environ
    env["PLAYGROUND_PATH"] = base_path

    for script in script_list:
        with tempfile.NamedTemporaryFile() as fp:
            if script.get("description"):
                print(f"- Running script {script.get('description')}")
            fp.file.write(script_header.encode())
            fp.file.write(script["run"].encode())
            fp.file.close()
            script_file = fp.name
            os.chmod(script_file, stat.S_IRWXU)
            run_command(script_file, None, None)


def start_kind(base_path):
    kind_config_file = os.path.join(base_path,"kind.yaml")
    playground_config_file = os.path.join(base_path,"playground.yaml")

    with open(kind_config_file) as fp:
        kind_config = yaml.safe_load(fp)

    with open(playground_config_file) as fp:
        playground_config = yaml.safe_load(fp)

    print("### Preparing local Kind")
    kind_check = f'kind get kubeconfig --name {kind_config["name"]}'
    if run_command(kind_check)["return_code"] != 0:
        kind_start = f"kind create cluster --config {kind_config_file}"
        run_command(kind_start, None, None)
    else:
        print("- Kind cluster already exist, skipping creation")

    print("\n### Running Post Start Scripts")
    run_scripts(playground_config["postStart"], base_path)


def stop_kind():
    pass