import os
from kubernetes import client, config
from kubernetes.client.rest import ApiException

def sync_secrets(source_namespace, target_namespaces, secret_name):
    # 加载Kubernetes配置
    config.load_kube_config()

    v1 = client.CoreV1Api()

    try:
        # 获取源命名空间中的指定Secret
        secret = v1.read_namespaced_secret(secret_name, source_namespace)

        for target_namespace in target_namespaces:
            # 创建一个新的Secret对象
            new_secret = client.V1Secret(
                metadata=client.V1ObjectMeta(name=secret.metadata.name),
                data=secret.data,
                type=secret.type
            )

            try:
                # 尝试在目标命名空间中创建Secret
                v1.create_namespaced_secret(target_namespace, new_secret)
                print(f"Secret {secret.metadata.name} 同步到命名空间 {target_namespace}")
            except ApiException as e:
                if e.status == 409:
                    # 如果Secret已经存在，则更新它
                    v1.replace_namespaced_secret(secret.metadata.name, target_namespace, new_secret)
                    print(f"Secret {secret.metadata.name} 更新到命名空间 {target_namespace}")
                else:
                    print(f"无法同步Secret {secret.metadata.name} 到命名空间 {target_namespace}: {e}")

    except ApiException as e:
        print(f"无法获取命名空间 {source_namespace} 中的Secret {secret_name}: {e}")

if __name__ == "__main__":
    source_ns = os.getenv("SOURCE_NAMESPACE")
    target_ns_list = os.getenv("TARGET_NAMESPACES").split(",")
    secret_name = os.getenv("SECRET_NAME")

    if not source_ns or not target_ns_list or not secret_name:
        print("请设置环境变量 SOURCE_NAMESPACE, TARGET_NAMESPACES 和 SECRET_NAME")
    else:
        sync_secrets(source_ns, target_ns_list, secret_name)
