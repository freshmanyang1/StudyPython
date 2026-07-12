# Architect Checklist

设计沟通规则见 SKILL.md「设计沟通规则」章节，此处不再重复。

## .NET 架构审查

- 是否存在硬编码设备类型、Topic、协议字段或基础设施实现。
- 是否直接依赖具体数据库、MQTT Broker、Redis、HTTP/gRPC 客户端实现。
- 公共 DTO、API、接口是否保持长期稳定。
- 新增字段是否向后兼容。
- IO 是否使用 `async/await` 和 `CancellationToken`。
- 是否存在 `.Result`、`.Wait()` 或阻塞式异步调用。
- 异常是否分类明确，是否存在 `throw Exception()` 或吞异常。
- 日志是否避免输出完整 token、设备密钥和连接串。
- 模块职责是否清晰，是否有过深继承或基础类堆积。
- 是否优先使用组合、接口和策略模式。

## IoT 架构审查

- 是否写死设备类型、Topic、协议版本或 Broker 实现。
- MQTT Topic 是否有清晰命名、方向、版本和兼容策略。
- gRPC、MQTT、WebSocket、Redis 状态是否边界清晰。
- 设备 SDK 是否能兼容旧协议和旧设备。
- Worker 与 SDK 的帧协议是否保持同步。
- 访问端和设备端连接行为是否兼容浏览器限制。
- 状态字段是否能表达设备在线、Tunnel 开关、连接状态和 session 状态。
- 多设备、多协议、多 Worker 部署时是否还能扩展。

## Framework Design Guidelines 视角

- 名称是否表达长期语义，而不是当前实现细节。
- 公共 API 是否稳定、可发现、可组合。
- 抽象是否足够小且可替换，不暴露基础设施细节。
- 模块是否优先组合和接口，而不是深层继承或基础类堆积。
- 公共代码是否能脱离具体业务场景复用。

## Tunnel 特别规则

涉及 Tunnel 且项目启用 Tunnel profile 时，遵守对应 `.agents/context/TUNNEL_RULES.md`：先说明影响范围，协议/Topic/gRPC/token/密钥变更必须先确认。未启用 Tunnel profile 时，不要假设存在 `docs/tunnel-overview.md` 或 `docs/tunnel-protocol-alignment.md`。
