[中文](README_CN.md) | [English](README.md)

# SecSync

SecSync is a tool for synchronizing Secrets in a Kubernetes cluster.

## Features

- Supports synchronizing multiple Secrets from one namespace to multiple target namespaces
- Supports creating or updating Secrets in target namespaces
- Supports scheduled synchronization via Kubernetes CronJob

## Usage

### Environment Variables

- `SOURCE_NAMESPACE`: Source namespace
- `TARGET_NAMESPACES`: Target namespaces, separated by commas
- `SECRET_NAMES`: Names of the Secrets to be synchronized, separated by commas

### Deployment

Modify the relevant configurations in the deploy directory, then

```bash
kubectl apply -k deploy/
```

## Telegram Channel

My Telegram channel: [https://t.me/bboysoulcn](https://t.me/bboysoulcn)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
