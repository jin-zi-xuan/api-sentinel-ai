# API Sentinel AI

API Sentinel AI 是一个用于应聘展示的 FastAPI 项目，定位为 AI 驱动的 API 安全测试与风险分析平台。

项目目标是导入 OpenAPI 文档，自动生成 API 资产清单，并在后续阶段使用 AI 生成安全测试用例，执行 API 安全测试，最终输出风险分析报告。

## 技术栈

- Python 3.11+
- FastAPI
- SQLAlchemy 2.x
- Pydantic v2
- Uvicorn
- SQLite（开发阶段默认数据库）
- Pytest

## 当前项目结构

```text
app/
  api/v1/        API 路由层
  core/          配置与核心能力
  db/            数据库连接与会话
  models/        SQLAlchemy 数据模型
  schemas/       Pydantic 数据结构
  crud/          数据访问逻辑
  services/      业务服务层
  utils/         通用工具
tests/           测试用例
docs/            项目文档
```

## 核心功能规划

- OpenAPI 文档导入与解析
- API 资产自动发现与入库
- AI 辅助生成安全测试用例
- 安全测试任务编排与执行
- 风险评分与问题分级
- 测试报告与风险分析报告生成

## 开发阶段路线

### Phase 1: 项目骨架

- 初始化 FastAPI 项目结构
- 配置 SQLAlchemy、Pydantic v2 与基础环境变量
- 提供健康检查接口
- 增加统一响应结构、异常处理、日志配置和基础测试

### Phase 2: OpenAPI 资产管理

- 支持上传或导入 OpenAPI 文档
- 解析接口路径、方法、参数、请求体与响应结构
- 建立 API 资产模型与基础 CRUD

### Phase 3: AI 测试用例生成

- 基于 API 资产生成安全测试思路
- 生成边界值、鉴权、注入、越权等测试用例
- 保留人工审核与调整入口

### Phase 4: 安全测试执行

- 执行测试任务
- 记录请求、响应、断言结果与异常信息
- 支持任务状态追踪

### Phase 5: 风险报告

- 汇总风险项
- 提供风险等级、影响范围与修复建议
- 生成面向展示的安全分析报告

## 启动方式

创建虚拟环境并安装依赖：

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

复制环境变量示例：

```bash
cp .env.example .env
```

启动开发服务：

```bash
uvicorn app.main:app --reload
```

初始化数据库：

```bash
python -m app.db.init_db
```

运行测试：

```bash
pytest
```

访问健康检查接口：

```bash
curl http://127.0.0.1:8000/health
```

预期响应：

```json
{
  "success": true,
  "code": "OK",
  "message": "Success",
  "data": {
    "status": "ok",
    "service": "API Sentinel AI",
    "version": "0.1.0"
  }
}
```

## 当前说明

当前版本包含项目骨架、健康检查、统一响应、异常处理、日志配置、数据库初始化入口和基础测试，暂未实现用户认证、AI 调用或安全扫描能力。
