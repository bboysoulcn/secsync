[中文](README_CN.md) | [English](README.md)

# SecSync

SecSync 是一个用于在 Kubernetes 集群中同步 Secrets 的工具。

## 特性

- 支持从一个命名空间同步多个 Secrets 到多个目标命名空间
- 支持在目标命名空间中创建或更新 Secrets
- 支持通过 Kubernetes CronJob 定时同步

## 使用

### 环境变量

- `SOURCE_NAMESPACE`: 源命名空间
- `TARGET_NAMESPACES`: 目标命名空间，多个命名空间用逗号分隔
- `SECRET_NAMES`: 要同步的 Secret 名称，多个名称用逗号分隔


### 部署

修改deploy中相关配置，然后


```bash
kubectl apply -k deploy/
```

## Telegram 频道

我的 Telegram 频道: [https://t.me/bboysoulcn](https://t.me/bboysoulcn)

## 许可证

这个项目使用 MIT 许可证，详情请见  [LICENSE](LICENSE) 文件。