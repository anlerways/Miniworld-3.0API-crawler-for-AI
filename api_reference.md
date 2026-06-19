# 《迷你世界》UGC 3.0 API 参考手册
> GitHub开源仓库: https://github.com/anlerways/Miniworld-3.0API-crawler-for-AI
> 本文档由爬虫自动生成，数据来源：https://dev-wiki.mini1.cn/ugc-wiki/

## Actor
### `ActorHurt`
**描述**: 对象造成伤害
**参数**:
- `objid` (number) — 攻击者对象ID
- `targetid` (number) — 目标对象ID
- `damage` (number) — 伤害值
- `attacktype` (number) — 伤害类型枚举(HurtType) HurtType
- `ignoreResist` (boolean) — 忽略伤害抵抗
- `ignoreTriggerEvent` (boolean) — 忽略触发伤害事件
**返回值**:
- `bool` (boolean) — 是否造成伤害成功

---
### `AddHp`
**描述**: 增加角色当前生命值
**参数**:
- `objid` (number) — 角色对象ID
- `hp` (number) — 血量值(hp>0增加血量,hp<0减少血量)
**返回值**:
- `bool` (boolean) — 是否操作成功

---
### `AddTags`
**描述**: 添加标签
**参数**:
- `objid` (number) — 对象ID
- `tags` (string / table) — 标签或标签数组(数值字母下划线组合)
- `icount` (number) — 引用计数(默认1)
**返回值**:
- `bool` (boolean) — 是否添加成功

---
### `AppendSpeed`
**描述**: 附加速度
**参数**:
- `objid` (number) — 对象ID
- `vx` (number) — 轴向速度X
- `vy` (number) — 轴向速度Y
- `vz` (number) — 轴向速度Z
**返回值**:
- `bool` (boolean) — 是否附加成功

---
### `ChangActorMoveType`
**描述**: 改变移动方式
**参数**:
- `objid` (number) — 对象ID
- `moveMode` (number) — 移动模式枚举(MoveType) MoveType
**返回值**:
- `bool` (boolean) — 是否改变成功(角色没有对应能力时返回失败)

---
### `ChangeCustomModel`
**描述**: 改变对象外观
**参数**:
- `objid` (number) — 对象ID
- `modleName` (string) — 对象外观描述
**返回值**:
- `bool` (boolean) — 是否改变成功

---
### `ClearActorWithId`
**描述**: 清除指定类型生物
**参数**:
- `actorid` (number / string) — 生物类型ID
- `bkill` (boolean) — 是否杀死生物(默认false，影响是否产生掉落物)
- `worldId` (number) — 星球ID(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否清除成功

---
### `ClearTags`
**描述**: 清空所有标签
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `bool` (boolean) — 是否清空成功

---
### `CompareMainModel`
**描述**: 比较主模型外观
**参数**:
- `facade1` (string) — 外观类型1
- `facade2` (string) — 外观类型2
**返回值**:
- `bool` (boolean) — 是否相等(参数错误返回false)

---
### `DisMountActor`
**描述**: 角色取消骑乘
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `bool` (boolean) — 是否取消成功

---
### `DropActor`
**描述**: 尝试投掷角色
**参数**:
- `objid` (number) — 投掷动作对象ID
- `dir` (table) — 投掷方向{x=number,y=number,z=number}
- `isThrow` (boolean) — 是否投掷
- `speed` (number) — 投掷速度
- `hasInertance` (boolean) — 是否有惯性
**返回值**:
- `bool` (boolean) — 是否投掷成功

---
### `EscapePickup`
**描述**: 尝试逃脱抓举
**参数**:
- `objid` (number) — 被抓举的对象ID
**返回值**:
- `bool` (boolean) — 是否逃脱成功

---
### `FindNearestBlock`
**描述**: 查找最近方块
**参数**:
- `objid` (number) — 对象ID
- `blockid` (number / string) — 查找的方块类型ID
- `blockRange` (number) — 查找范围(传1表示1格方块距离)
**返回值**:
- `x` (number) — 方块坐标X
- `y` (number) — 方块坐标Y
- `z` (number) — 方块坐标Z(失败返回nil)

---
### `GetActorFacade`
**描述**: 获取角色外观
**参数**:
- `objid` (number) — 对象ID
- `bhasequip` (boolean) — 是否包含装备(默认false，仅玩家有效)
**返回值**:
- `facade` (string) — 对象外观描述信息(失败返回nil)

---
### `GetActorMovementMode`
**描述**: 获取移动模式
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `num` (number) — 移动模式枚举(MoveType)(失败返回nil)

---
### `GetActorPermissions`
**描述**: 获取对象权限
**参数**:
- `objid` (number) — 对象ID
- `ability` (number) — 行为枚举(Ability) Ability
**返回值**:
- `bool` (boolean) — 权限开关状态

---
### `GetAttr`
**描述**: 获取角色属性值
**参数**:
- `objid` (number) — 角色对象ID
- `atttype` (number) — 属性类型枚举(RoleAttr) RoleAttr
**返回值**:
- `num` (number) — 属性值(失败返回nil)

---
### `GetBoundSzie`
**描述**: 获取模型大小
**参数**:
- `objid` (number) — 角色对象ID
**返回值**:
- `vec` (table) — 模型大小{x=长,y=高,z=宽}(失败返回nil)

---
### `GetBtreeVarValue`
**描述**: 获取行为树变量
**参数**:
- `objid` (number) — 生物对象ID
- `varid` (string) — 变量ID
**返回值**:
- `val` (any变量值(失败返回nil，组数据无法获取))

---
### `GetDropItemInstanceId`
**描述**: 获取掉落物实例ID
**参数**:
- `objid` (number) — 掉落物对象ID
**返回值**:
- `id` (string) — 道具实例ID(失败返回nil)

---
### `GetDropItemNum`
**描述**: 获取掉落物品数量
**参数**:
- `objid` (number) — 掉落物对象ID
**返回值**:
- `num` (number) — 掉落物品数量

---
### `GetEntityFacade`
**描述**: 获取实体类型外观
**参数**:
- `prefab` (string) — 实体类型名称
**返回值**:
- `facade` (string) — 外观描述信息(失败返回nil)

---
### `GetEyeHeight`
**描述**: 获取角色眼睛高度
**参数**:
- `objid` (number) — 角色对象ID
**返回值**:
- `num` (number) — 眼睛高度(失败返回nil)

---
### `GetFaceDirection`
**描述**: 获取对象朝向
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `pos` (table) — 轴向上的方向向量{x=number,y=number,z=number}(失败返回nil)

---
### `GetFacePitch`
**描述**: 获取仰望角度
**参数**:
- `objid` (number) — 生物对象ID
**返回值**:
- `num` (number) — 仰望角度(失败返回nil)

---
### `GetFaceYaw`
**描述**: 获取面向角度
**参数**:
- `objid` (number) — 生物对象ID
**返回值**:
- `num` (number) — 面朝角度(失败返回nil)

---
### `GetItemId`
**描述**: 获取掉落物类型ID
**参数**:
- `objid` (number) — 掉落物对象ID
**返回值**:
- `id` (number) — 掉落物类型ID(失败返回nil)

---
### `GetMaxHP`
**描述**: 获取最大生命值
**参数**:
- `objid` (number) — 角色对象ID
**返回值**:
- `num` (number) — 最大生命值(失败返回nil)

---
### `GetMotion`
**描述**: 获取对象移动速度
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `x` (number) — 运动速度X
- `y` (number) — 运动速度Y
- `z` (number) — 运动速度Z(未移动时速度为0)

---
### `GetNickName`
**描述**: 获取角色昵称
**参数**:
- `objid` (number) — 角色对象ID
**返回值**:
- `name` (string) — 角色昵称(失败返回nil)

---
### `GetObjType`
**描述**: 获取对象类型
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `itype` (number) — 对象类型枚举(ObjType)(失败返回nil)

---
### `GetObjWorldId`
**描述**: 获取角色所在星球ID
**参数**:
- `objid` (number) — 角色对象ID
**返回值**:
- `id` (number) — 星球ID(失败返回-1)

---
### `GetPickupObjID`
**描述**: 获取举起行为中的角色ID
**参数**:
- `objid` (number) — 角色对象ID
- `roleType` (number) — 角色类型(1=举起者CARRYING, 2=被举起者CARRIED)
**返回值**:
- `id` (number) — 角色对象ID(失败返回0)

---
### `GetPosition`
**描述**: 获取对象位置
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `x` (number) — 目标X坐标
- `y` (number) — 目标Y坐标
- `z` (number) — 目标Z坐标(失败返回nil)

---
### `GetRidingActorObjId`
**描述**: 获取骑乘生物ID
**参数**:
- `objid` (number) — 角色对象ID
**返回值**:
- `id` (number) — 生物对象ID(失败返回0)

---
### `GetTags`
**描述**: 获取对象标签列表
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `tags` (table) — 标签数组(失败返回nil)

---
### `GetTeam`
**描述**: 获取角色队伍
**参数**:
- `objid` (number) — 角色对象ID
**返回值**:
- `id` (number) — 队伍ID(失败返回nil)

---
### `HasTags`
**描述**: 对象是否有标签
**参数**:
- `objid` (number) — 对象ID
- `tags` (string / table) — 标签或标签数组
- `mathcmode` (number) — 匹配方式(MatchMode) MatchMode
- `bexactmatch` (boolean) — 每条标签是否精确匹配
**返回值**:
- `bool` (boolean) — 是否具有标签

---
### `IncreasesAttr`
**描述**: 增加角色属性值
**参数**:
- `objid` (number) — 角色对象ID
- `atttype` (number) — 属性类型枚举(RoleAttr) RoleAttr
- `val` (number) — 增加值
**返回值**:
- `bool` (boolean) — 是否增加成功

---
### `IsExist`
**描述**: 对象是否存在
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `bool` (boolean) — 是否存在

---
### `IsPlayer`
**描述**: 检查对象是否为玩家
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `bool` (boolean) — 是否为玩家

---
### `Jump`
**描述**: 对象跳跃
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `bool` (boolean) — 是否跳跃成功

---
### `KillSelf`
**描述**: 击败对象
**参数**:
- `objid` (number) — 生物对象ID
**返回值**:
- `bool` (boolean) — 是否击败成功

---
### `MountActor`
**描述**: 角色骑乘
**参数**:
- `objid` (number) — 对象ID
- `rideobjid` (number) — 被骑乘对象ID
- `isContrl` (boolean) — 是否控制
- `isCloseAI` (boolean) — 是否关闭AI
**返回值**:
- `bool` (boolean) — 是否骑乘成功

---
### `PauseSoundEffectById`
**描述**: 暂停/恢复音效
**参数**:
- `objid` (number) — 角色对象ID
- `soundId` (number) — 声音ID(-1表示暂停所有音效)
- `pause` (boolean) — true暂停/false恢复
**返回值**:
- `bool` (boolean) — 是否操作成功

---
### `PickupActor`
**描述**: 角色举起角色
**返回值**:
- `bool` (boolean) — 是否举起成功

---
### `PickupItem`
**描述**: 角色拾取物品
**参数**:
- `objid` (number) — 角色对象ID
- `itemobjid` (number) — 掉落物或投掷物对象ID
- `bforcepickup` (boolean) — 是否强制拾取(默认false)
**返回值**:
- `num` (number) — 拾取数量(失败返回0)

---
### `PlayAnim`
**描述**: 对象播放动作
**参数**:
- `objid` (number) — 对象ID
- `animid` (number / string) — 动作ID
- `speed` (number) — 播放速度
- `loop` (number / boolean) — 播放模式(AnimMode)或是否循环 AnimMode
**返回值**:
- `bool` (boolean) — 是否播放成功

---
### `PlayAnimByObj`
**描述**: 对象播放对象动作
**参数**:
- `objidA` (number) — 对象ID A
- `objidB` (number) — 对象ID B
- `breplay` (boolean) — 是否重新播放(默认false)
**返回值**:
- `bool` (boolean) — 是否播放成功(仅玩家、生物、实体生效)

---
### `PlayBodyParticleById`
**描述**: 播放粒子特效
**参数**:
- `objid` (number) — 生物对象ID
- `particleId` (number / string) — / table 粒子特效ID或ID数组
- `ptme` (number) — 时长(单位：秒)
- `offset` (table) — 偏移(默认{x=0,y=0,z=0})
- `rot` (table) — 旋转(默认{x=0,y=0,z=0})
- `scale` (table) — 缩放(默认{x=1,y=1,z=1})
**返回值**:
- `bool` (boolean) — 是否播放成功

---
### `PlayHandAnim`
**描述**: 对象手持播放动作
**参数**:
- `objid` (number) — 对象ID
- `animid` (number / string) — 动作ID
- `speed` (number) — 播放速度
- `loop` (number / boolean) — 播放模式(AnimMode)或是否循环 AnimMode
**返回值**:
- `bool` (boolean) — 是否播放成功

---
### `PlaySoundEffectById`
**描述**: 播放音效
**参数**:
- `objid` (number) — 角色对象ID
- `soundId` (number) — 声音ID
- `volume` (number) — 音量(0-100，实际会转换为0-1)
- `pitch` (number) — 音调(默认1.0)
- `isLoop` (boolean) — 是否循环播放(默认false)
**返回值**:
- `bool` (boolean) — 是否播放成功

---
### `RandomFacadeID`
**描述**: 随机外观ID
**返回值**:
- `id` (string) — 随机外观ID(失败返回nil)

---
### `RecoverinitialModel`
**描述**: 恢复对象外观
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `bool` (boolean) — 是否恢复成功

---
### `RemoveTags`
**描述**: 删除标签
**参数**:
- `objid` (number) — 对象ID
- `tags` (string / table) — 标签或标签数组
- `icount` (number) — 引用计数(默认0，传0全部删除)
**返回值**:
- `bool` (boolean) — 是否删除成功

---
### `RotateFaceToActor`
**描述**: 生物朝向目标
**参数**:
- `objid` (number) — 生物对象ID
- `targetid` (number) — 目标生物对象ID
**返回值**:
- `bool` (boolean) — 是否旋转成功

---
### `SetAblePick`
**描述**: 设置掉落物可拾取
**参数**:
- `objid` (number) — 掉落物对象ID
- `able` (boolean) — 是否可以拾取
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetActorPermissions`
**描述**: 设置对象权限
**参数**:
- `objid` (number) — 对象ID
- `ability` (number) — 行为枚举(Ability) Ability
- `switch` (boolean) — 是否开启
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetAttr`
**描述**: 设置角色属性
**参数**:
- `objid` (number) — 角色对象ID
- `atttype` (number) — 属性类型枚举(RoleAttr) RoleAttr
- `val` (number) — 属性值
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetBeHurtTarget`
**描述**: 设置仇恨目标
**参数**:
- `objid` (number) — 生物对象ID
- `targetid` (number) — 目标生物对象ID
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetBodyParticleTransform`
**描述**: 设置粒子特效变换
**参数**:
- `objid` (number) — 生物对象ID
- `particleId` (number / string) — / table 粒子特效ID或ID数组
- `offset` (table) — 偏移(默认{x=0,y=0,z=0})
- `rot` (table) — 旋转(默认{x=0,y=0,z=0})
- `scale` (table) — 缩放(默认{x=1,y=1,z=1})
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetBtreeVarValue`
**描述**: 设置行为树变量
**参数**:
- `objid` (number) — 生物对象ID
- `varid` (string) — 变量ID
- `val` (any变量值)
**返回值**:
- `bool` (boolean) — 是否设置成功(组数据无法设置)

---
### `SetFaceDirection`
**描述**: 设置对象朝向
**参数**:
- `objid` (number) — 对象ID
- `x` (number) — 轴向方向X
- `y` (number) — 轴向方向Y
- `z` (number) — 轴向方向Z
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetFacePitch`
**描述**: 设置仰望角度
**参数**:
- `objid` (number) — 生物对象ID
- `pitch` (number) — 仰望角度
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetFaceYaw`
**描述**: 设置面向角度
**参数**:
- `objid` (number) — 生物对象ID
- `yaw` (number) — 面朝角度
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetImmuneType`
**描述**: 设置免疫伤害类型
**参数**:
- `objid` (number) — 对象ID
- `immunetype` (number) — 伤害类型枚举(HurtType，-1表示免疫所有伤害) HurtType
- `isadd` (boolean) — 是否开启免疫
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetNickName`
**描述**: 设置角色昵称
**参数**:
- `objid` (number) — 角色对象ID
- `nickname` (string) — 昵称
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetPosition`
**描述**: 设置角色位置
**参数**:
- `objid` (number) — 角色对象ID
- `x` (number) — 目标X坐标
- `y` (number) — 目标Y坐标
- `z` (number) — 目标Z坐标
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetTeam`
**描述**: 设置角色队伍
**参数**:
- `objid` (number) — 角色对象ID
- `teamid` (number) — 队伍ID(AbsoluteCampType) AbsoluteCampType
- `bResetAttr` (boolean) — 是否重置属性(仅玩家有效，默认false)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `ShowNickName`
**描述**: 设置昵称显示
**参数**:
- `objid` (number) — 角色对象ID
- `bshow` (boolean) — 是否显示昵称
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `StopBodyEffectById`
**描述**: 停止粒子特效
**参数**:
- `objid` (number) — 生物对象ID
- `particleId` (number / string) — / table 粒子特效ID或ID数组
**返回值**:
- `bool` (boolean) — 是否停止成功

---
### `StopSoundEffectById`
**描述**: 停止音效
**参数**:
- `objid` (number) — 角色对象ID
- `soundId` (number) — 声音ID
**返回值**:
- `bool` (boolean) — 是否停止成功

---
### `TryMoveToActor`
**描述**: 对象移动到目标
**参数**:
- `objid` (number) — 执行动作的对象ID
- `targetObjid` (number) — 目标对象ID
- `speed` (number) — 移动速度
**返回值**:
- `bool` (boolean) — 是否移动成功

---
### `TryMoveToPos`
**描述**: 移动对象到位置（寻路）
**参数**:
- `objid` (number) — 角色对象ID
- `x` (number) — 目标X坐标
- `y` (number) — 目标Y坐标
- `z` (number) — 目标Z坐标
- `cancontrol` (boolean) — 是否能控制(默认true)
- `bshowtip` (boolean) — 是否显示提示(默认false)
**返回值**:
- `bool` (boolean) — 是否移动成功

---
### `TryPickupActorForward`
**描述**: 尝试抓取前方对象
**参数**:
- `objid` (number) — 角色对象ID
- `distance` (number) — 抓取距离
**返回值**:
- `bool` (boolean) — 是否抓取成功

---

## Area
### `BlockInArea`
**描述**: 检测区域内是否有某个方块
**参数**:
- `areaid` (number) — 区域ID
- `blockid` (number / string) — 方块类型ID
**返回值**:
- `bool` (boolean) — 是否在区域内

---
### `CheckRangeCanPlace`
**描述**: 检查指定范围内是否可以放置方块
**参数**:
- `posbeg` (table) — 区域起始位置
- `posend` (table) — 区域结束位置
- `blockid` (string / number) — 方块ID
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否可以放置方块

---
### `ClearAllBlock`
**描述**: 清空区域内全部方块
**参数**:
- `areaid` (number) — 区域唯一ID
- `blockid` (number / string) — 方块类型ID
- `num` (number) — 最大清除数量
- `btriggerevent` (boolean) — 是否触发事件(默认false)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `ClearAllBlockAreaRange`
**描述**: 清空区域范围内方块
**参数**:
- `posbeg` (table) — 起始位置
- `posend` (table) — 末点位置
- `blockid` (number / string) — 方块类型
- `btriggerevent` (boolean) — 是否触发事件
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `CloneAreaBlock`
**描述**: 复制区域内方块到另一个区域
**参数**:
- `areaid` (number) — 区域唯一ID
- `pos` (table) — 目标起始位置
**返回值**:
- `bool` (boolean) — 是否成功

---
### `CloneAreaRange`
**描述**: 复制区域范围内方块到另一个区域
**参数**:
- `posbeg` (table) — 起始位置
- `posend` (table) — 末点位置
- `deststartpos` (table) — 目标起始位置
- `itype` (number) — 操作类型
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 操作是否成功

---
### `CreateAreaPrefab`
**描述**: 创建区域对象
**参数**:
- `pos` (table) — 区域底部中心位置
- `size` (table) — 区域大小
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `obj` (table) — 区域对象
- `id` (number) — 区域对象ID

---
### `CreateAreaRectByRange`
**描述**: 创建矩形区域
**参数**:
- `posBeg` (table) — 区域起始坐标
- `posEnd` (table) — 区域结束坐标
- `btmp` (boolean) — 是否是临时区域
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `id` (number) — 区域ID

---
### `DestroyAllBlock`
**描述**: 破坏区域内的方块
**参数**:
- `areaid` (number) — 区域ID
- `blockid` (string / number) — 方块ID或资产ID
- `n` (number) — 销毁数量(不填或者0则全部销毁)
- `candrop` (boolean) — 是否掉落物品
- `btriggerevent` (boolean) — 是否触发事件
**返回值**:
- `bool` (boolean) — 操作是否成功

---
### `DestroyArea`
**描述**: 销毁区域
**参数**:
- `areaid` (number) — 区域ID
**返回值**:
- `bool` (boolean) — 是否成功

---
### `FillBlockAreaRange`
**描述**: 用方块填充区域范围
**参数**:
- `posbeg` (table) — 起始位置
- `posend` (table) — 末点位置
- `blockid` (number / string) — 方块类型
- `face` (number) — 朝向
- `color` (string / number) — 颜色
- `switch` (boolean) — 是否开启
- `filltype` (number) — 填充类型(AreaFillType) AreaFillType
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `GetAllCreaturesInAreaRange`
**描述**: 获取区域范围内全部生物
**参数**:
- `posbeg` (table) — 起始位置
- `posend` (table) — 末点位置
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `objids` (table) — 对象ID组

---
### `GetAllObjsInAreaRange`
**描述**: 获取区域范围内全部对象
**参数**:
- `posbeg` (table) — 起始位置
- `posend` (table) — 末点位置
- `objtype` (number) — 对象类型(ObjType) ObjType
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `objids` (table) — 对象ID组

---
### `GetAllPlayersInAreaRange`
**描述**: 获取区域范围内全部玩家
**参数**:
- `posbeg` (table) — 起始位置
- `posend` (table) — 末点位置
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `objids` (table) — 对象ID组

---
### `GetAreaBlockTypes`
**描述**: 获取区域内的方块类型
**参数**:
- `areaid` (number) — 区域ID
**返回值**:
- `ids` (table) — 方块类型ID组

---
### `GetAreaCenter`
**描述**: 获取区域中间点
**参数**:
- `areaid` (number) — 区域ID
**返回值**:
- `pos` (table) — 区域中心位置

---
### `GetAreaCreatures`
**描述**: 获取区域中的所有生物
**参数**:
- `areaid` (number) — 区域唯一ID
**返回值**:
- `objids` (table) — 生物ID组

---
### `GetAreaPlayers`
**描述**: 获取区域中的所有玩家
**参数**:
- `areaid` (number) — 区域唯一ID
**返回值**:
- `objids` (table) — 玩家ID组

---
### `GetAreaRectLength`
**描述**: 获取区域各边长
**参数**:
- `areaid` (number) — 区域ID
**返回值**:
- `lenx` (number) — x轴向长度
- `leny` (number) — y轴向长度
- `lenz` (number) — z轴向长度

---
### `GetAreaRectRange`
**描述**: 获取区域范围
**参数**:
- `areaid` (number) — 区域ID
**返回值**:
- `posBeg` (table) — 区域起始坐标
- `posEnd` (table) — 区域结束坐标
- `worldId` (number) — 星球id

---
### `GetAreaUuidByObjId`
**描述**: 通过区域对象ID获取区域uuid
**参数**:
- `objId` (number) — 区域对象ID
**返回值**:
- `id` (number) — 区域uuid

---
### `GetBlockNum`
**描述**: 获取区域内的方块数量
**参数**:
- `areaid` (number) — 区域ID
- `blockid` (string / number) — 方块ID
**返回值**:
- `num` (number) — 方块数量

---
### `GetRandomAirPos`
**描述**: 获取一个区域内随机空气方块
**参数**:
- `posbeg` (table) — 区域起始位置
- `posend` (table) — 区域结束位置
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `pos` (table) — 随机空气位置(x,y,z)

---
### `GetRandomPos`
**描述**: 随机区域内位置
**参数**:
- `areaid` (number) — 区域ID
**返回值**:
- `pos` (table) — 随机坐标

---
### `GetRelativeActors`
**描述**: 获取区域中指定玩家关系的角色
**参数**:
- `posbeg` (table) — 区域起始位置
- `posend` (table) — 区域结束位置
- `uin` (number) — 玩家ID
- `relativing` (number) — 关系类型(RelativeCampType) RelativeCampType
- `actortype` (number) — 角色(ObjType) ObjType
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `num` (number) — 数量
- `ids` (table) — ID数组

---
### `ObjInArea`
**描述**: 检测对象是否在区域内
**参数**:
- `areaid` (number) — 区域ID
- `objid` (number) — 对象ID
**返回值**:
- `bool` (boolean) — 是否在区域内

---
### `PosInArea`
**描述**: 位置是否在区域内
**参数**:
- `areaid` (number) — 区域唯一ID
- `pos` (table) — 位置(x|y|z)
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否在区域内

---
### `ReplaceAreaBlock`
**描述**: 替换方块类型为新的方块类型
**参数**:
- `areaid` (number) — 区域唯一ID
- `srcblockid` (number / string) — 区域内的方块类型
- `destblockid` (number / string) — 替换的方块类型
- `face` (number) — 方块朝向
- `color` (string / number) — 颜色
**返回值**:
- `bool` (boolean) — 是否成功

---
### `ReplaceAreaRangeBlock`
**描述**: 替换区域范围方块
**参数**:
- `posbeg` (table) — 起始位置
- `posend` (table) — 末点位置
- `srcblockid` (number / string) — 方块类型
- `destblockid` (number / string) — 目标方块类型
- `face` (number) — 朝向
- `inair` (boolean) — 是否包括空气方块
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 操作是否成功

---

## Array
### `Clear`
**描述**: 清空数组
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
**返回值**:
- `bool` (boolean) — 是否清空成功

---
### `GetAllValue`
**描述**: 获取数组所有数据
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
**返回值**:
- `values` (table) — 数组所有值(失败返回空表{})

---
### `GetCountByValue`
**描述**: 获取值出现次数
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
- `value` (any具体值)
**返回值**:
- `num` (number) — 值出现的次数(失败返回0)

---
### `GetIndexByValue`
**描述**: 获取值对应的索引位置
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
- `value` (any具体值)
**返回值**:
- `num` (number) — 索引位置(失败返回nil)

---
### `GetMax`
**描述**: 获取数组最大值
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
**返回值**:
- `num` (number) — 最大值(失败返回nil)

---
### `GetMin`
**描述**: 获取数组最小值
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
**返回值**:
- `num` (number) — 最小值(失败返回nil)

---
### `GetSize`
**描述**: 获取数组长度
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
**返回值**:
- `num` (number) — 数组元素数量(失败返回0)

---
### `GetValue`
**描述**: 获取数组值
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
- `index` (number) — 索引
**返回值**:
- `value` (any数组值(失败返回nil))

---
### `HasValue`
**描述**: 数组是否有值
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
- `value` (any具体值)
**返回值**:
- `bool` (boolean) — 是否包含该值

---
### `HasValueByNo`
**描述**: 数组索引是否有值
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
- `ix` (number) — 索引
**返回值**:
- `bool` (boolean) — 该索引位置是否有值

---
### `IncreasesValue`
**描述**: 增加数组值
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
- `value` (number) — 增加值
- `index` (number) — 索引
**返回值**:
- `bool` (boolean) — 是否增加成功

---
### `InsertValue`
**描述**: 插入数组值
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
- `value` (any具体值)
- `index` (number) — 索引(可选，为空则添加到末尾)
**返回值**:
- `bool` (boolean) — 是否插入成功

---
### `InsertValues`
**描述**: 数组合并插入
**参数**:
- `varId1` (string) — 目标数组ID
- `playerId1` (number) — 目标数组玩家uin(全局数组传nil)
- `index` (number) — 插入索引(可选，为空则添加到末尾)
- `varId2` (string) — 源数组ID
- `playerId2` (number) — 源数组玩家uin(全局数组传nil)
**返回值**:
- `bool` (boolean) — 是否插入成功

---
### `RandomValue`
**描述**: 获取数组随机值
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
**返回值**:
- `value` (any随机元素值(失败返回nil))

---
### `Remove`
**描述**: 删除数组值
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
- `index` (number) — 索引
**返回值**:
- `bool` (boolean) — 是否删除成功

---
### `RemoveByValue`
**描述**: 删除数组值
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
- `value` (any具体值)
**返回值**:
- `bool` (boolean) — 是否删除成功

---
### `RemoveByValues`
**描述**: 删除数组中相同值
**参数**:
- `varId1` (string) — 目标数组ID
- `playerId1` (number) — 目标数组玩家uin(全局数组传nil)
- `varId2` (string) — 源数组ID
- `playerId2` (number) — 源数组玩家uin(全局数组传nil)
**返回值**:
- `bool` (boolean) — 是否删除成功

---
### `ReplaceValue`
**描述**: 替换数组值
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
- `value` (any新值)
- `oldValue` (any旧值)
**返回值**:
- `bool` (boolean) — 是否替换成功

---
### `SetValue`
**描述**: 设置数组值
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
- `value` (any具体值)
- `index` (number) — 索引
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `Sort`
**描述**: 数组排序
**参数**:
- `varId` (string) — 数组ID
- `playerId` (number) — 玩家uin(全局数组传nil)
- `isUp` (number) — 排序方式(SortType) SortType
**返回值**:
- `bool` (boolean) — 是否排序成功

---

## Backpack
### `ActDestructEquip`
**描述**: 销毁装备
**参数**:
- `playerid` (number) — 玩家ID
- `grid` (number) — 装备栏ID（EquipStartIndex + EquipSlotType.Head是装备栏第一个格子，EquipSlotType.Weapon无效） EquipSlotType
**返回值**:
- `bool` (boolean) — 是否成功

---
### `ActEquipOffByEquipID`
**描述**: 脱下装备
**参数**:
- `playerid` (number) — 玩家ID
- `grid` (number) — 装备栏ID（EquipStartIndex + EquipSlotType.Head是装备栏第一个格子，EquipSlotType.Weapon无效） EquipSlotType
- `togrid` (number) — 目标格子ID（可不传，如果不为nil则必须是空格子）
**返回值**:
- `bool` (boolean) — 是否成功

---
### `ActEquipUpByResID`
**描述**: 穿上装备
**参数**:
- `playerid` (number) — 玩家ID
- `itemid` (number / string) — 道具类型
- `frompos` (number) — 格子ID（可不传，如果不为nil则必须和itemid一致）
**返回值**:
- `bool` (boolean) — 是否成功

---
### `AddItem`
**描述**: 添加道具到背包
**参数**:
- `playerid` (number) — 玩家ID
- `itemid` (number / string) — 道具类型
- `num` (number) — 道具数量
- `prioritytype` (number) — 优先存放位置（1优先快捷栏，2优先背包栏，默认1）
**返回值**:
- `num` (number) — 成功添加的数量

---
### `CalcSpaceNumForItem`
**描述**: 计算背包剩余空间
**参数**:
- `playerid` (number) — 玩家ID
- `itemid` (number / string) — 道具类型
**返回值**:
- `num` (number) — 可以存放的数量

---
### `ClearAllPack`
**描述**: 清空全部背包
**参数**:
- `playerid` (number) — 玩家ID
**返回值**:
- `bool` (boolean) — 是否成功

---
### `ClearGrids`
**描述**: 批量清理背包格
**参数**:
- `playerid` (number) — 玩家ID
- `begingridId` (number) — 开始格子ID
- `endgridId` (number) — 结束格子ID
**返回值**:
- `bool` (boolean) — 是否成功

---
### `ClearPack`
**描述**: 清空背包栏
**参数**:
- `playerid` (number) — 玩家ID
- `bartype` (number) — 快捷栏枚举(BackpackType) BackpackType
**返回值**:
- `bool` (boolean) — 是否成功

---
### `CreateGunInBackpack`
**描述**: 创建枪械到背包
**参数**:
- `playerid` (number) — 玩家Uin
- `itemid` (number / string) — 道具ID
- `gridIndex` (number / nil) — 格子索引（nil表示自动选择）
**返回值**:
- `id` (string) — 道具实例ID

---
### `CreateItem`
**描述**: 创建道具到背包
**参数**:
- `objid` (number) — 玩家ID
- `itemid` (number / string) — 道具类型
- `itemnum` (number) — 道具数量
- `ipos` (number) — 优先存放的位置
**返回值**:
- `bool` (boolean) — 是否成功

---
### `CreateItemInstInBackpack`
**描述**: 创建道具实例到背包
**参数**:
- `playerid` (number) — 玩家Uin
- `itemid` (number / string) — 道具ID
- `gridIndex` (number / nil) — 格子索引（nil表示自动选择）
**返回值**:
- `id` (string) — 道具实例ID

---
### `DecodeGridInfo`
**描述**: 解析格子信息
**参数**:
- `str` (string) — GetGridInfos打包字符串
**返回值**:
- `obj` (table) — 解析后的数组（数组元素包含index格子ID、info格子详细信息、itemid物品ID、num数量，nil表示解析失败）

---
### `DiscardItem`
**描述**: 丢弃背包格道具
**参数**:
- `playerid` (number) — 玩家ID
- `gridid` (number) — 格子ID
- `num` (number) — 道具数量
- `ablePick` (boolean) — 是否允许拾取
**返回值**:
- `bool` (boolean) — 是否成功

---
### `DiscardItemByID`
**描述**: 通过道具ID丢弃道具
**参数**:
- `playerid` (number) — 玩家ID
- `itemid` (number / string) — 道具ID
- `itemnum` (number) — 道具数量
**返回值**:
- `bool` (boolean) — 是否成功

---
### `EncodeTableGridInfo`
**描述**: 打包格子信息
**参数**:
- `infos` (table) — DecodeGridInfo解析后的数据
**返回值**:
- `value` (string) — 打包后的字符串（nil表示打包失败，否则成功）

---
### `EnoughSpaceForItem`
**描述**: 检查背包空间是否足够
**参数**:
- `playerid` (number) — 玩家ID
- `itemid` (number / string) — 道具类型
- `num` (number) — 道具数量(默认1)
**返回值**:
- `bool` (boolean) — 是否有足够空间

---
### `GetAllBackPackInstanceIds`
**描述**: 获取背包所有道具实例ID
**参数**:
- `playerid` (number) — 玩家ID
- `bartype` (number) — 快捷栏枚举(BackpackType) BackpackType
**返回值**:
- `ids` (table) — 道具实例ID数组

---
### `GetGridAttr`
**描述**: 获取背包格属性
**参数**:
- `playerid` (number) — 玩家ID
- `gridid` (number) — 格子ID
- `attr` (number) — 属性枚举(GridAttr) GridAttr
**返回值**:
- `num` (number) — 属性值

---
### `GetGridInfos`
**描述**: 批量获取背包格信息
**参数**:
- `playerid` (number) — 玩家ID
- `begingridId` (number) — 开始格子ID
- `endgridId` (number) — 结束格子ID
**返回值**:
- `value` (string) — 格子信息字符串（nil表示失败，否则成功）

---
### `GetGridItemID`
**描述**: 获取背包格道具ID
**参数**:
- `playerid` (number) — 玩家ID
- `gridid` (number) — 格子ID (BackpackBeginIndex.Shortcut + 0 是快捷栏第一个格子) BackpackBeginIndex
**返回值**:
- `itemid` (number / string) — 道具类型
- `num` (number) — 道具数量（无道具时数量为0，itemid为0）

---
### `GetGridItemName`
**描述**: 获取背包格道具名称
**参数**:
- `playerid` (number) — 玩家ID
- `gridid` (number) — 格子ID
**返回值**:
- `name` (string) — 道具名称

---
### `GetGunInstIdInBackpack`
**描述**: 获取背包所有枪械实例ID
**参数**:
- `playerid` (number) — 玩家Uin
**返回值**:
- `ids` (table) — 枪械实例ID数组

---
### `GetInstIdByGridIndex`
**描述**: 根据背包索引获取道具实例ID
**参数**:
- `playerid` (number) — 玩家Uin
- `gridIndex` (number) — 背包索引
**返回值**:
- `id` (string) — 道具实例ID

---
### `GetItemNum`
**描述**: 获取背包道具数量
**参数**:
- `playerid` (number) — 玩家ID
- `itemid` (number / string) — 道具类型
- `isAddEquip` (boolean) — 是否包含装备栏(默认True)
**返回值**:
- `num` (number) — 道具总数量
- `ids` (table) — 装有道具的格子ID数组

---
### `GetItemNumByBackpackBar`
**描述**: 获取背包栏道具数量
**参数**:
- `playerid` (number) — 玩家ID
- `bartype` (number) — 快捷栏枚举(BackpackType) BackpackType
- `itemid` (number / string) — 道具类型
**返回值**:
- `num` (number) — 道具总数量
- `ids` (table) — 装有道具的格子ID数组

---
### `HasItemByBackpackBar`
**描述**: 检测背包是否持有道具
**参数**:
- `playerid` (number) — 玩家ID
- `bartype` (number) — 快捷栏枚举(BackpackType) BackpackType
- `itemid` (number / string) — 道具类型
**返回值**:
- `bool` (boolean) — 是否持有
- `id` (number) — 道具所在格子ID（如果持有）

---
### `IsLock`
**描述**: 获取背包格是否锁定
**参数**:
- `playerid` (number) — 玩家Uin
- `gridIndex` (number) — 格子索引
**返回值**:
- `bool` (boolean) — 是否锁定（参数错误返回true）

---
### `LoadGridInfos`
**描述**: 加载背包和快捷栏格子信息数据
**参数**:
- `playerid` (number) — 玩家ID
- `gridinfo` (string) — 格子信息字符串（由GetGridInfos返回）
**返回值**:
- `bool` (boolean) — 是否成功

---
### `MoveGridItem`
**描述**: 移动背包道具
**参数**:
- `playerid` (number) — 玩家ID
- `gridsrc` (number) — 源格子ID
- `griddst` (number) — 目标格子ID
- `num` (number) — 道具数量(默认全部)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `PlayShortCutItemParticle`
**描述**: 手持指定道具播放粒子特效
**参数**:
- `playerid` (number) — 玩家ID
- `itemid` (number) — 道具类型
- `effectids` (number / string) — / table 特效ID或特效名称或ID数组
- `offset` (table) — 偏移向量{x,y,z}
- `rot` (table) — 旋转向量{x,y,z}
- `scale` (table) — 缩放向量{x,y,z}
**返回值**:
- `bool` (boolean) — 是否成功

---
### `PlayShortCutIxParticle`
**描述**: 手持道具播放粒子特效
**参数**:
- `playerid` (number) — 玩家ID
- `effectids` (number / string) — / table 特效ID或特效名称或ID数组
- `offset` (table) — 偏移向量{x,y,z}
- `rot` (table) — 旋转向量{x,y,z}
- `scale` (table) — 缩放向量{x,y,z}
**返回值**:
- `bool` (boolean) — 是否成功

---
### `RemoveGridItem`
**描述**: 移除背包格道具
**参数**:
- `playerid` (number) — 玩家ID
- `gridid` (number) — 格子ID
- `num` (number) — 道具数量(默认全部移除)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `RemoveGridItemByItemID`
**描述**: 通过道具ID移除背包道具
**参数**:
- `playerid` (number) — 玩家ID
- `itemid` (number / string) — 道具类型
- `num` (number) — 道具数量
**返回值**:
- `num` (number) — 移除数量（num and num> 0 成功）

---
### `SetBackPackNum`
**描述**: 设置背包数量
**参数**:
- `playerid` (number) — 玩家ID
- `num` (number) — 背包格子数量（范围0-100）
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetGridAttr`
**描述**: 设置背包格属性
**参数**:
- `playerid` (number) — 玩家ID
- `gridid` (number) — 格子ID
- `attr` (number) — 属性枚举(GridAttr) GridAttr
- `value` (number) — 属性值
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetGridItem`
**描述**: 设置背包格道具
**参数**:
- `playerid` (number) — 玩家ID
- `gridid` (number) — 格子ID
- `itemid` (number / string) — 道具类型
- `num` (number) — 道具数量(默认1)
- `durability` (number) — 耐久值(默认1)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetGridsLock`
**描述**: 设置背包格锁定状态
**参数**:
- `playerid` (number) — 玩家ID
- `begingridId` (number) — 开始格子ID
- `endgridId` (number) — 结束格子ID
- `lock` (boolean) — 是否锁定（true锁定，false解锁）
**返回值**:
- `bool` (boolean) — 是否成功

---
### `StopShortCutItemEffect`
**描述**: 手持指定道具停止特效
**参数**:
- `playerid` (number) — 玩家ID
- `itemid` (number) — 道具类型
- `effectids` (number / string) — / table 特效ID或特效名称或ID数组
**返回值**:
- `bool` (boolean) — 是否成功

---
### `StopShortCutIxEffect`
**描述**: 手持道具停止特效
**参数**:
- `playerid` (number) — 玩家ID
- `effectids` (number / string) — / table 特效ID或特效名称或ID数组
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SwapGridItem`
**描述**: 交换背包道具
**参数**:
- `playerid` (number) — 玩家ID
- `gridsrc` (number) — 源格子ID
- `griddst` (number) — 目标格子ID
**返回值**:
- `bool` (boolean) — 是否成功

---

## Block
### `DestroyBlock`
**描述**: 摧毁方块
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `dropitem` (boolean) — 是否掉落物品(默认false)
- `worldId` (number) — 星球id(默认当前主机所在星球)
- `btrigger` (boolean) — 是否触发全局事件(默认true)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `GetBlockData`
**描述**: 获取方块数据
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `num` (number) — 方块data数据值

---
### `GetBlockDefDesc`
**描述**: 获取方块描述
**参数**:
- `blockid` (number / string) — 方块类型ID
**返回值**:
- `value` (string) — 方块描述

---
### `GetBlockDefName`
**描述**: 获取方块名称
**参数**:
- `blockid` (number / string) — 方块类型ID
**返回值**:
- `name` (string) — 方块名称

---
### `GetBlockDir`
**描述**: 获取方块朝向
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `num` (number) — 方块朝向（FaceDir枚举）

---
### `GetBlockDropExp`
**描述**: 获取方块采集经验
**参数**:
- `blockid` (number / string) — 方块ID
**返回值**:
- `num` (number) — 经验值

---
### `GetBlockDropItemType`
**描述**: 获取方块掉落物信息
**参数**:
- `blockid` (number / string) — 方块ID
- `itype` (number) — 类型（1手持敲方块，2手持道具正确，3手持道具不正确）
**返回值**:
- `obj` (table) — 掉落道具信息{itemid,itemnum,odds} 道具ID、数量、概率

---
### `GetBlockID`
**描述**: 获取方块类型ID
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `id` (number) — 方块类型ID

---
### `GetBlockPowerStatus`
**描述**: 获取方块通电状态
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否通电

---
### `GetBlockSettingAttState`
**描述**: 获取方块属性状态
**参数**:
- `blockid` (number / string) — 方块类型ID
- `atttype` (number) — 属性枚举(BlockLimits) BlockLimits
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否开启

---
### `GetBlockSwitchStatus`
**描述**: 获取功能方块开关状态
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否开启

---
### `GetFacade`
**描述**: 获取方块类型外观
**参数**:
- `blockid` (number / string) — 方块类型ID或方块预制ID
**返回值**:
- `value` (string) — 方块类型外观

---
### `IsAirBlock`
**描述**: 判断是否为空气方块
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否为空气方块

---
### `IsLiquidBlock`
**描述**: 判断是否为液体方块
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否为液体方块

---
### `IsSolidBlock`
**描述**: 判断是否为固体方块
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否为固体方块

---
### `PlaceBlock`
**描述**: 放置方块
**参数**:
- `blockid` (number / string) — 方块类型ID
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `face` (number) — 朝向(默认0)
- `color` (number / string) — 十六进制颜色值(0XFFFFFF 颜色方块类型才生效，默认-1)
- `worldId` (number) — 星球id(默认当前主机所在星球)
- `btrigger` (boolean) — 是否触发全局事件(默认true)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `PlayAnim`
**描述**: 播放方块动作
**参数**:
- `pos` (table) — 位置坐标{x=x,y=y,z=z}
- `animid` (number / string) — 动作ID
- `speed` (number) — 播放速度(默认1)
- `loop` (number) — 循环模式(AnimMode枚举) AnimMode
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `PlayCrackEffect`
**描述**: 播放方块裂纹特效
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `process` (number) — 进度(-1~10)
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `PlayDestroyEffect`
**描述**: 播放方块损毁特效
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `RandomBlockID`
**描述**: 随机获取方块ID
**返回值**:
- `id` (number) — 随机的方块类型ID

---
### `ReplaceBlock`
**描述**: 替换方块
**参数**:
- `blockid` (number / string) — 方块类型ID
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `face` (number) — 朝向(默认0)
- `color` (number / string) — 十六进制颜色值(0XFFFFFF 颜色方块类型才生效，默认-1)
- `worldId` (number) — 星球id(默认当前主机所在星球)
- `btrigger` (boolean) — 是否触发全局事件(默认true)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `ReplaceBluePrint`
**描述**: 放置蓝图
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `blueprint` (string) — 蓝图资源ID
- `angle` (number) — 旋转角度
- `mirror` (boolean) — 是否镜像
- `placeMode` (boolean) — 是否蓝图区域全部覆盖
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetBlockColor`
**描述**: 设置方块颜色
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `color` (number) — 颜色值
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetBlockData`
**描述**: 设置方块数据
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `data` (number) — 方块数据
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetBlockDir`
**描述**: 设置方块方向
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `dir` (number) — 方向值(FaceDir枚举) FaceDir
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetBlockSettingAttState`
**描述**: 设置方块属性状态
**参数**:
- `blockid` (number / string) — 方块类型ID
- `atttype` (number) — 属性枚举(BlockLimits) BlockLimits
- `switch` (boolean) — 是否开启
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetBlockSwitchStatus`
**描述**: 设置功能方块开关状态
**参数**:
- `x` (number) — 位置X坐标
- `y` (number) — 位置Y坐标
- `z` (number) — 位置Z坐标
- `isactive` (boolean) — 是否开启
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetBlockTextureColor`
**描述**: 设置方块纹理颜色
**参数**:
- `blockid` (number) — 方块ID
- `color` (number:颜色值(0:还原默认颜色))
- `alpha` (number) — 混合比例(0-100)
- `slotindex` (number) — 材质槽索引(默认1)
**返回值**:
- `bool` (boolean) — 是否成功

---

## Buff
### `AddBuff`
**描述**: 附加效果
**参数**:
- `objid` (number) — 对象ID
- `buffid` (number / string) — 效果ID
- `customticks` (number) — 效果持续时间(-1表示默认配置，0表示无限)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `ClearAllBadBuff`
**描述**: 清除所有负面效果
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `bool` (boolean) — 是否成功

---
### `ClearAllBuff`
**描述**: 清除所有效果
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `bool` (boolean) — 是否成功

---
### `ClearAllGoodBuff`
**描述**: 清除所有有益效果
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `bool` (boolean) — 是否成功

---
### `GetBuffDefDesc`
**描述**: 获取效果描述
**参数**:
- `buffid` (number / string) — 效果ID
**返回值**:
- `value` (string) — 状态效果描述

---
### `GetBuffDefName`
**描述**: 获取效果名称
**参数**:
- `buffid` (number / string) — 效果ID
**返回值**:
- `name` (string) — 效果名称

---
### `GetBuffLeftTime`
**描述**: 获取效果剩余时间
**参数**:
- `objid` (number) — 对象ID
- `buffid` (number / string) — 效果ID
**返回值**:
- `num` (number) — 剩余时间(秒，0表示永久)

---
### `GetBuffList`
**描述**: 获取效果列表
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `num` (number) — 效果数量
- `ids` (table) — 效果ID数组

---
### `GetBuffNumByBuffid`
**描述**: 获取效果数量
**参数**:
- `objid` (number) — 对象ID
- `buffid` (number / string) — 效果ID
**返回值**:
- `num` (number) — 效果数量

---
### `HasBuff`
**描述**: 判断是否有效果
**参数**:
- `objid` (number) — 对象ID
- `buffid` (number / string) — 效果ID
**返回值**:
- `bool` (boolean) — 是否有该效果

---
### `RemoveBuff`
**描述**: 移除效果
**参数**:
- `objid` (number) — 对象ID
- `buffid` (number / string) — 效果ID
**返回值**:
- `bool` (boolean) — 是否成功

---
### `ReplaceBuff`
**描述**: 替换效果
**参数**:
- `objid` (number) — 对象ID
- `buffsrc` (number / string) — 源状态ID
- `buffdst` (number / string) — 目标状态ID
- `customticks` (number) — 持续时间(默认-1)
**返回值**:
- `bool` (boolean) — 是否成功

---

## Chat
### `SendSystemMsg`
**描述**: 发送系统消息
**参数**:
- `content` (string) — 消息
- `playerID` (number) — 玩家ID 0表示发给所有玩家
**返回值**:
- `ret` (boolean) — 成功(true)

---

## CustomUI
### `ChangeParent`
**描述**: 修改元件父元件
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `parentElementid` (string) — 父元件ID
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `CloneElement`
**描述**: 克隆元件
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 被克隆元件ID
**返回值**:
- `elementid` (string) — 克隆元件ID；失败返回nil/false

---
### `CreateElement`
**描述**: 动态创建元件
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementType` (number) — 元件类型枚举(ElementType) ElementType
**返回值**:
- `elementid` (string) — 新建元件ID；失败返回nil/false

---
### `DeleteElement`
**描述**: 删除UI元件
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
**返回值**:
- `bool` (boolean) — 是否删除成功

---
### `GetBlockIcon`
**描述**: 获取方块图标
**参数**:
- `blockid` (number / string) — 方块类型ID/预制ID
**返回值**:
- `icon` (string) — 方块图标标识；无效返回""

---
### `GetItemIcon`
**描述**: 获取道具图标
**参数**:
- `itemid` (number / string) — 道具类型ID/预制ID
**返回值**:
- `icon` (string) — 道具图标标识；失败返回""

---
### `GetMonsterIcon`
**描述**: 获取生物图标(类型)
**参数**:
- `actorid` (number / string) — 生物类型ID/预制ID
**返回值**:
- `icon` (string) — 生物图标标识；无效返回""

---
### `GetMonsterObjIcon`
**描述**: 获取生物图标(对象)
**参数**:
- `objid` (number) — 对象ID
**返回值**:
- `icon` (string) — 生物图标标识；无效返回""

---
### `GetProgressBarValue`
**描述**: 获取进度条值
**参数**:
- `reportid` (number) — 上报ID
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
**返回值**:
- `bool` (boolean) — 是否上报成功

---
### `GetRoleHeadIcon`
**描述**: 获取角色头像图标
**参数**:
- `playerid` (number) — 玩家ID
**返回值**:
- `icon` (string) — 头像图标标识

---
### `GetRoleIcon`
**描述**: 获取角色图标
**参数**:
- `playerid` (number) — 玩家ID
**返回值**:
- `icon` (string) — 角色图标标识；失败返回nil

---
### `GetScreenSize`
**描述**: 获取屏幕分辨率
**参数**:
- `playerid` (number) — 玩家ID
**返回值**:
- `Width` (number) — 屏幕宽度
- `Height` (number) — 屏幕高度

---
### `GetShortcutIcon`
**描述**: 获取快捷栏图标
**参数**:
- `playerid` (number) — 玩家ID
- `ix` (number) — 快捷栏索引(1-8)
**返回值**:
- `icon` (string) — 道具图标标识；失败返回nil

---
### `GetStatusIcon`
**描述**: 获取状态图标
**参数**:
- `buffid` (number / string) — 状态ID/预制ID
**返回值**:
- `icon` (string) — 状态图标标识；无效返回""或nil

---
### `HideElement`
**描述**: 隐藏元件
**参数**:
- `objid` (number) — 玩家/对象ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `effectid` (number) — 动画ID(可选)
- `time` (number) — 动画时长(可选)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `PlayElementAnim`
**描述**: 播放元件动画
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `animid` (number) — 动画ID
- `time` (number) — 单次执行时间(需大于0)
- `mode` (number) — 播放模式(AnimMode) AnimMode
- `easetype` (number) — 缓动类型(Easing,可选) Easing
- `delaytime` (number) — 延迟播放时间(可选)
- `endvalue` (number / table) — 动画结束值(可选)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `RotateElement`
**描述**: 旋转元件
**参数**:
- `objid` (number) — 玩家/对象ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `rotate` (number) — 旋转角度
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetAlpha`
**描述**: 设置透明度
**参数**:
- `objid` (number) — 玩家/对象ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `alpha` (number) — 透明度(0~100)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetBeaconBandPos`
**描述**: 设置信标位置
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `bandPosX` (number) — x坐标
- `bandPosY` (number) — y坐标
- `bandPosZ` (number) — z坐标
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetBeaconClampType`
**描述**: 设置信标限制范围
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `clampRange` (number) — 限制类型
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetBeaconMapType`
**描述**: 设置信标映射类型
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `mapType` (number) — 映射类型(0位置/1对象)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetBeaconMargin`
**描述**: 设置信标矩形范围
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `rectMinX` (number) — minX
- `rectMinY` (number) — minY
- `rectMaxX` (number) — maxX
- `rectMaxY` (number) — maxY
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetBeaconObjId`
**描述**: 设置信标对象
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `objId` (number) — 对象ID
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetBeaconOffset`
**描述**: 设置信标偏移
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `offsetX` (number) — x偏移
- `offsetY` (number) — y偏移
- `offsetZ` (number) — z偏移
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetBeaconRadius`
**描述**: 设置信标半径
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `radius` (number) — 半径
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetColor`
**描述**: 设置文本元件颜色
**参数**:
- `objid` (number) — 玩家/对象ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `color` (number) — 颜色值(0xFFFFFF)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetFloatDamageTxt`
**描述**: 设置浮动伤害文本
**参数**:
- `playerid` (number) — 玩家ID
- `elementid` (string) — 元件ID
- `objid` (number) — 对象ID
- `text` (string) — 文本
- `color` (number) — 颜色(可选)
- `offsetx` (number) — X偏移(可选)
- `offsety` (number) — Y偏移(可选)
- `movex` (number) — 移动X(可选)
- `movey` (number) — 移动Y(可选)
- `showtime` (number) — 显示时长(可选)
- `movex2` (number) — 移动X2(可选)
- `movey2` (number) — 移动Y2(可选)
- `showtime2` (number) — 显示时长2(可选)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetFontSize`
**描述**: 设置文本元件字体大小
**参数**:
- `objid` (number) — 玩家/对象ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `size` (number) — 字体大小
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetLoaderModel`
**描述**: 设置装载器模型
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `modleName` (string) — 模型名称(如ItemInstance_xxx/avator_xxx等) stance
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetLoaderModelAct`
**描述**: 设置装载器模型动画
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `animid` (number / string) — 动画ID
- `playmode` (number) — 播放模式(AnimMode) AnimMode
- `speed` (number) — 播放速度(0~1)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetLoaderModelDir`
**描述**: 设置装载器模型方向
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `yaw` (number) — 水平角度(角度制)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetLoaderModelPosition`
**描述**: 设置装载器模型位置
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `x` (number) — x坐标
- `y` (number) — y坐标
- `z` (number) — z坐标
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetLoaderModelScale`
**描述**: 设置装载器模型缩放
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `modlescale` (number) — 缩放大小
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetPosition`
**描述**: 设置元件位置
**参数**:
- `objid` (number) — 玩家/对象ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `x` (number) — X坐标值
- `y` (number) — Y坐标值
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetProgressBarResId`
**描述**: 设置进度条纹理
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `itype` (number) — 类型枚举(ProgressImg) ProgressImg
- `url` (string) — 图片资源ID
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetProgressBarValue`
**描述**: 设置进度条值
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `itype` (number) — 类型枚举(ProgressVal) ProgressVal
- `value` (number) — 设定值
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetRelationPosition`
**描述**: 设置元件相对位置
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `v` (number) — 水平偏移枚举(HorizontalOffset) HorizontalOffset
- `xOffset` (number) — X偏移值
- `xUnits` (number) — 单位枚举(PixelUnits) PixelUnits
- `h` (number) — 垂直偏移枚举(VerticalOffset) VerticalOffset
- `yOffset` (number) — Y偏移值
- `yUnits` (number) — 单位枚举(PixelUnits) PixelUnits
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetRelationSize`
**描述**: 设置元件相对大小
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `width` (number) — 宽度值
- `widthUnits` (number) — 单位枚举(PixelUnits) PixelUnits
- `height` (number) — 高度值
- `heightUnits` (number) — 单位枚举(PixelUnits) PixelUnits
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetScale`
**描述**: 设置元件缩放
**参数**:
- `objid` (number) — 玩家/对象ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `x` (number) — X缩放
- `y` (number) — Y缩放
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetSize`
**描述**: 设置元件大小
**参数**:
- `objid` (number) — 玩家/对象ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `width` (number) — 元件宽度
- `height` (number) — 元件高度
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetSliderBarImg`
**描述**: 设置滑动条图案
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `url` (string) — 图片资源ID/链接
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetSliderDir`
**描述**: 设置滑动列表滑动方式
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `dir` (number) — 滑动方式(0仅左右/1仅上下/2自由滑动)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetSpineAnimID`
**描述**: 设置Spine动画ID
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `animid` (number) — 内置动画ID
- `animindex` (number) — 动画序列
- `playmode` (number) — 播放模式(ViedoPlayMode) ViedoPlayMode
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetState`
**描述**: 设置界面状态
**参数**:
- `objid` (number) — 玩家/对象ID
- `uiid` (string) — 界面ID
- `pageIndex` (string) — 状态ID
- `easeType` (number) — 缓动类型(Easing)(可选) Easing
- `time` (number) — 过渡时长(可选)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetText`
**描述**: 设置文本元件内容
**参数**:
- `objid` (number) — 玩家/对象ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `text` (string) — 文本内容
- `animid` (number) — 动画ID(可选)
- `time` (number) — 动画时长(可选)
- `mode` (number) — 播放模式(可选)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SetTexture`
**描述**: 设置元件图案纹理
**参数**:
- `objid` (number) — 玩家/对象ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `url` (string) — 图案纹理ID
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `ShowElement`
**描述**: 显示元件
**参数**:
- `objid` (number) — 玩家/对象ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `effectid` (number) — 动画ID(可选)
- `time` (number) — 动画时长(可选)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SmoothChangeProgress`
**描述**: 进度条文本平滑变化
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `bval` (number) — 开始值
- `eval` (number) — 结束值
- `time` (number) — 执行时间
**返回值**:
- `bool` (boolean) — 是否触发成功(无显式返回值时为nil)

---
### `SmoothIncreaseProgress`
**描述**: 进度条文本平滑变化(增减)
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `time` (number) — 时长
- `ptype` (number) — 类型(1增加/2减小/3变化至)
- `value` (number) — 变化值
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SmoothMoveBy`
**描述**: 元件平滑移动相对距离
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `time` (number) — 执行时间(需大于0)
- `x` (number) — X方向距离
- `y` (number) — Y方向距离
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SmoothMoveTo`
**描述**: 元件平滑移动到指定位置
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `time` (number) — 执行时间(需大于0)
- `x` (number) — X坐标(可选)
- `y` (number) — Y坐标(可选)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SmoothRotateBy`
**描述**: 元件平滑旋转相对角度
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `time` (number) — 执行时间(需大于0)
- `angle` (number) — 角度增量
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SmoothRotateTo`
**描述**: 元件平滑旋转到指定角度
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `time` (number) — 执行时间(需大于0)
- `angle` (number) — 角度值
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SmoothScaleBy`
**描述**: 元件平滑改变相对宽高
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `time` (number) — 执行时间(需大于0)
- `w` (number) — 宽度增量
- `h` (number) — 高度增量
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SmoothScaleByEx`
**描述**: 元件平滑缩放(扩展)
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `time` (number) — 执行时间(需大于0)
- `x` (number) — X缩放值
- `y` (number) — Y缩放值
- `delayTime` (number) — 延迟时间(可选)
- `easeType` (number) — 缓动枚举(Easing,可选) Easing
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `SmoothScaleTo`
**描述**: 元件平滑缩放到指定尺寸
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `time` (number) — 执行时间(需大于0)
- `w` (number) — 宽度(可选)
- `h` (number) — 高度(可选)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `StopAnim`
**描述**: 停止元件动画
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `itype` (number) — 停止类型(0全部/1指定元件)
**返回值**:
- `bool` (boolean) — 是否设置成功

---
### `TurnSliderToPos`
**描述**: 滑动列表跳转到位置
**参数**:
- `playerid` (number) — 玩家ID
- `uiid` (string) — 界面ID
- `elementid` (string) — 元件ID
- `x` (number) — X坐标值
- `y` (number) — Y坐标值
**返回值**:
- `bool` (boolean) — 是否设置成功

---

## Data
### `GetValue`
**描述**: 获取变量值
**参数**:
- `varId` (string) — 变量ID
- `playerId` (number) — 玩家ID(全局变量传nil)
**返回值**:
- `value` (any变量值；失败或无值返回nil)

---
### `IncreasesValue`
**描述**: 数值变量增加值
**参数**:
- `varId` (string) — 变量ID
- `playerId` (number) — 玩家ID(全局变量传nil)
- `value` (number) — 增加的量
**返回值**:
- `num` (number) — 增加后的值；参数错误返回nil

---
### `SetValue`
**描述**: 设置变量值
**参数**:
- `varId` (string) — 变量ID
- `playerId` (number) — 玩家ID(全局变量传nil)
- `value` (any设置的值)
**返回值**:
- `bool` (boolean) — 是否设置成功

---

## GameObject
### `CreatePrefab`
**描述**: 创建对象列表
**参数**:
- `objectType` (number) — 对象类型(ObjType) ObjType
- `prefabId` (number / string) — 类型ID或预制ID
- `x` (number) — X坐标
- `y` (number) — Y坐标
- `z` (number) — Z坐标
- `num` (number) — 数量(可选)
- `trigger` (boolean) — 是否触发事件(可选)
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `objids` (table) — 创建对象列表(安全对象)；失败返回nil

---
### `CreatePrefabInst`
**描述**: 使用预制ID创建对象
**参数**:
- `prefabId` (string) — 预制体ID
- `worldId` (number) — 星球ID(可选)
- `x` (number) — X坐标
- `y` (number) — Y坐标
- `z` (number) — Z坐标
- `trigger` (boolean) — 是否触发事件(可选)
**返回值**:
- `obj` (object创建的游戏对象；失败返回nil)

---
### `Destroy`
**描述**: 删除对象
**参数**:
- `objId` (number / string) — 对象ID
**返回值**:
- `bool` (boolean) — 是否删除成功

---
### `FindBlockObject`
**描述**: 查找方块类别对象
**参数**:
- `id` (number / string) — 方块类型ID
**返回值**:
- `obj` (object方块类别对象；未找到返回nil)

---
### `FindObject`
**描述**: 根据ID查找游戏对象
**参数**:
- `id` (number / string) — 游戏对象唯一标识
**返回值**:
- `obj` (object游戏对象；未找到返回nil)

---
### `FindUIObject`
**描述**: 获取UI对象
**参数**:
- `id` (number / string) — UI对象唯一标识
**返回值**:
- `obj` (objectUI游戏对象；未找到返回nil)

---
### `GetObjectPrefab`
**描述**: 获取对象预制ID
**参数**:
- `objId` (number) — 对象ID
**返回值**:
- `id` (number / string) — 预制ID
- `num` (number) — 对象类型(多返回值)；失败返回nil

---

## Graphics
### `CreateBrushByPos`
**描述**: 在位置上创建笔刷
**参数**:
- `pos` (table) — 位置坐标{x,y,z}
- `dim` (table) — 尺寸{x,y,z}
- `color` (number / string) — 颜色值(0xFFFFFF)
- `showuin` (number) — 显示玩家Uin(0全部)
- `itype` (number) — 类别ID
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `id` (number) — 笔刷实例ID；失败返回false

---
### `CreateGraphicsArrowByActorToActor`
**描述**: 生物指向生物箭头
**参数**:
- `objid` (number) — 对象ID
- `info` (table) — 图文信息
- `dir` (table) — 方向{x,y,z}
- `offset` (number) — 方向偏移距离
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsArrowByActorToPos`
**描述**: 生物指向位置箭头
**参数**:
- `objid` (number) — 对象ID
- `info` (table) — 图文信息(MakeGraphicsArrowToPos等) Graphics
- `dir` (table) — 方向{x,y,z}
- `offset` (number) — 方向偏移距离
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsArrowByPosToActor`
**描述**: 位置指向生物箭头
**参数**:
- `pos` (table) — 位置坐标{x,y,z}
- `info` (table) — 图文信息
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsArrowByPosToPos`
**描述**: 位置指向位置箭头
**参数**:
- `pos` (table) — 位置坐标{x,y,z}
- `info` (table) — 图文信息
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsImageByActor`
**描述**: 在生物上创建图像
**参数**:
- `objid` (number) — 对象ID
- `info` (table) — 图文信息
- `dir` (table) — 方向{x,y,z}
- `offest` (number) — 方向偏移距离
- `x2` (number) — X偏移(可选)
- `y2` (number) — Y偏移(可选)
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsImageByPos`
**描述**: 在位置上创建图像
**参数**:
- `x` (number) — 方块X
- `y` (number) — 方块Y
- `z` (number) — 方块Z
- `info` (table) — 图文信息(MakeGraphicsImage) Graphics
- `x2` (number) — X偏移(可选)
- `y2` (number) — Y偏移(可选)
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsLineByActorToActor`
**描述**: 生物到生物线
**参数**:
- `objid` (number) — 对象ID
- `info` (table) — 图文信息
- `dir` (table) — 方向{x,y,z}
- `offset` (number) — 方向偏移距离
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsLineByActorToPos`
**描述**: 生物到位置线
**参数**:
- `objid` (number) — 对象ID
- `info` (table) — 图文信息
- `dir` (table) — 方向{x,y,z}
- `offset` (number) — 方向偏移距离
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsLineByPosToActor`
**描述**: 位置到生物线
**参数**:
- `pos` (table) — 位置坐标{x,y,z}
- `info` (table) — 图文信息
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsLineByPosToPos`
**描述**: 位置到位置线
**参数**:
- `pos` (table) — 位置坐标{x,y,z}
- `info` (table) — 图文信息
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsNavPathByActorToPos`
**描述**: 生物到位置寻路引导线
**参数**:
- `objid` (number) — 对象ID
- `info` (table) — 图文信息(含pos、id、tCanSeePlayers等) Player
- `dir` (table) — 方向{x,y,z}
- `offset` (number) — 方向偏移距离
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsProgressByActor`
**描述**: 在生物身上创建进度条
**参数**:
- `objid` (number) — 对象ID
- `info` (table) — 图文信息
- `dir` (table) — 方向{x,y,z}
- `offest` (number) — 方向偏移距离
- `x2` (number) — X偏移(可选)
- `y2` (number) — Y偏移(可选)
**返回值**:
- `id` (number) — 图文实例ID；失败返回nil

---
### `CreateGraphicsProgressByPos`
**描述**: 在位置上创建进度条
**参数**:
- `x` (number) — 方块X
- `y` (number) — 方块Y
- `z` (number) — 方块Z
- `info` (table) — 图文信息(MakeGraphicsProgress) Graphics
- `x2` (number) — X偏移(可选)
- `y2` (number) — Y偏移(可选)
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `id` (number) — 图文实例ID；失败返回nil

---
### `CreateGraphicsSurfaceByActorToActor`
**描述**: 生物到生物面
**参数**:
- `objid` (number) — 对象ID
- `info` (table) — 图文信息
- `dir` (table) — 方向{x,y,z}
- `offset` (number) — 方向偏移距离
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsSurfaceByActorToPos`
**描述**: 生物到位置面
**参数**:
- `objid` (number) — 对象ID
- `info` (table) — 图文信息
- `dir` (table) — 方向{x,y,z}
- `offset` (number) — 方向偏移距离
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsSurfaceByPosToActor`
**描述**: 位置到生物面
**参数**:
- `pos` (table) — 位置坐标{x,y,z}
- `info` (table) — 图文信息
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsSurfaceByPosToPos`
**描述**: 位置到位置面
**参数**:
- `pos` (table) — 位置坐标{x,y,z}
- `info` (table) — 图文信息
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `bool` (boolean) — 是否创建成功

---
### `CreateGraphicsTxtByActor`
**描述**: 在生物身上创建文字板
**参数**:
- `objid` (number) — 对象ID
- `info` (table) — 图文信息
- `dir` (table) — 方向{x,y,z}
- `offest` (number) — 方向偏移距离
- `x2` (number) — X偏移(可选)
- `y2` (number) — Y偏移(可选)
**返回值**:
- `id` (number) — 图文实例ID；失败返回nil

---
### `CreateGraphicsTxtByPos`
**描述**: 在位置上创建图文
**参数**:
- `x` (number) — 方块X
- `y` (number) — 方块Y
- `z` (number) — 方块Z
- `graphicInfo` (table) — 图文信息(MakeGraphicsText等) GraphicsT
- `x2` (number) — X偏移(可选)
- `y2` (number) — Y偏移(可选)
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `id` (number) — 图文实例ID；失败返回nil

---
### `CreateflotageTextByActor`
**描述**: 在生物身上创建漂浮文字
**参数**:
- `objid` (number) — 对象ID
- `info` (table) — 图文信息
- `dir` (table) — 方向{x,y,z}
- `offest` (number) — 方向偏移距离
- `x2` (number) — X偏移(可选)
- `y2` (number) — Y偏移(可选)
**返回值**:
- `id` (number) — 图文实例ID；失败返回nil

---
### `CreateflotageTextByPos`
**描述**: 在位置上创建漂浮文字
**参数**:
- `x` (number) — 方块X
- `y` (number) — 方块Y
- `z` (number) — 方块Z
- `info` (table) — 图文信息(MakeflotageText)
- `x2` (number) — X偏移(可选)
- `y2` (number) — Y偏移(可选)
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `id` (number) — 图文实例ID；失败返回nil

---
### `GetInnerGraphicsOffset`
**描述**: 获取内嵌图文偏移高度
**参数**:
- `tuin` (number) — 玩家Uin
- `itype` (number) — 类型(PlayerNameType) PlayerNameType
- `callback` (function回调函数(参数为高度值))

---
### `MakeGraphicsArrowToActor`
**描述**: 生成指向对象的箭头数据
**参数**:
- `objid` (number) — 对象ID
- `size` (number) — 缩放值(可选)
- `color` (number / string) — 颜色值(0xFFFFFF)
- `itype` (number) — 箭头ID
**返回值**:
- `obj` (table) — 箭头信息表；失败返回nil

---
### `MakeGraphicsArrowToPos`
**描述**: 生成指向位置的箭头数据
**参数**:
- `x` (number) — 方块X
- `y` (number) — 方块Y
- `z` (number) — 方块Z
- `size` (number) — 缩放值(可选)
- `color` (number / string) — 颜色值(0xFFFFFF)
- `itype` (number) — 箭头ID
**返回值**:
- `obj` (table) — 箭头信息表；失败返回nil

---
### `MakeGraphicsImage`
**描述**: 生成图片信息
**参数**:
- `imgid` (string) — 图片资源ID
- `scale` (number) — 缩放值(可选)
- `apha` (number) — 透明度(0~100,可选)
- `itype` (number) — 图片ID
**返回值**:
- `obj` (table) — 图片信息表；参数无效返回nil

---
### `MakeGraphicsLineToActor`
**描述**: 生成指向对象的线数据
**返回值**:
- `info` (table) — 线信息内容

---
### `MakeGraphicsLineToPos`
**描述**: 生成指向位置的线数据
**参数**:
- `x` (number) — 方块X
- `y` (number) — 方块Y
- `z` (number) — 方块Z
- `size` (number) — 缩放值(可选)
- `color` (number / string) — 颜色值(0xFFFFFF)
- `itype` (number) — 线ID
**返回值**:
- `obj` (table) — 线信息表；失败返回nil

---
### `MakeGraphicsNavPathToPos`
**描述**: 生成寻路引导线数据
**参数**:
- `x` (number) — 方块X
- `y` (number) — 方块Y
- `z` (number) — 方块Z
- `itype` (number) — 线ID
**返回值**:
- `obj` (table) — 寻路线信息表

---
### `MakeGraphicsProgress`
**描述**: 创建进度条信息
**参数**:
- `v1` (number) — 当前值
- `v2` (number) — 最大值
- `color` (number / string) — 颜色值(0xFFFFFF)
- `itype` (number) — 进度条ID
**返回值**:
- `obj` (table) — 进度条信息表；失败返回nil

---
### `MakeGraphicsSurfaceToActor`
**描述**: 生成指向对象的面数据
**返回值**:
- `info` (table) — 面信息内容

---
### `MakeGraphicsSurfaceToPos`
**描述**: 生成指向位置的面数据
**参数**:
- `x` (number) — 方块X
- `y` (number) — 方块Y
- `z` (number) — 方块Z
- `size` (number) — 缩放值(可选)
- `color` (number / string) — 颜色值(0xFFFFFF)
- `itype` (number) — 面ID
**返回值**:
- `obj` (table) — 面信息表；失败返回nil

---
### `MakeGraphicsText`
**描述**: 创建文字板信息
**参数**:
- `title` (string) — 文本内容
- `font` (number) — 字体大小
- `apha` (number) — 不透明度
- `itype` (number) — 文字板ID
- `autoWrap` (number) — 是否自动换行(默认1)
**返回值**:
- `obj` (table) — 文字板信息表；失败返回nil

---
### `MakeflotageText`
**描述**: 创建漂浮文字信息
**参数**:
- `title` (string) — 文本内容
- `font` (number) — 字体大小
- `itype` (number) — 漂浮文字ID
**返回值**:
- `obj` (table) — 漂浮文字信息表；失败返回nil

---
### `RemoveGraphicsByGraphicsID`
**描述**: 按ID删除图文
**参数**:
- `objid` (number) — 图文实例ID
**返回值**:
- `bool` (boolean) — 是否删除成功

---
### `RemoveGraphicsByObjID`
**描述**: 删除生物的图文
**参数**:
- `objid` (number) — 对象ID
- `itype` (number) — 图文实例ID
- `graphType` (number) — 图文类型枚举(Graphics) Graphics
**返回值**:
- `bool` (boolean) — 是否删除成功

---
### `RemoveGraphicsByPos`
**描述**: 删除位置上的图文
**参数**:
- `x` (number) — 方块X
- `y` (number) — 方块Y
- `z` (number) — 方块Z
- `itype` (number) — 图文实例ID
- `graphType` (number) — 图文类型枚举(Graphics) Graphics
- `worldId` (number) — 星球ID(可选)
**返回值**:
- `bool` (boolean) — 是否删除成功

---
### `ReplaceAllGraphics`
**描述**: 迁移所有图文到目标对象
**参数**:
- `srcObjid` (number) — 源对象ID
- `desObjid` (number) — 目标对象ID
**返回值**:
- `bool` (boolean) — 是否迁移成功

---
### `UpdateGraphicsProgressById`
**描述**: 更新进度条进度
**参数**:
- `graphid` (number) — 图文实例ID
- `val1` (number) — 当前值
- `val2` (number) — 最大值
- `isync` (boolean) — 是否同步到客机(可选)
**返回值**:
- `bool` (boolean) — 是否更新成功

---
### `UpdateGraphicsTextById`
**描述**: 更新文字板内容
**参数**:
- `graphid` (number) — 图文实例ID
- `title` (string) — 文本内容
- `fontsize` (number) — 字体大小
- `apha` (number) — 不透明度
- `isync` (boolean) — 是否同步到客机(可选)
**返回值**:
- `bool` (boolean) — 是否更新成功

---

## Item
### `AddSubModelPart`
**描述**: 给道具实例添加一个模型子部件
**参数**:
- `instId` (string) — 道具实例id
- `partName` (string) — 子部件名字
- `boneName` (string) — 挂点
- `modelStr` (string) — 模型
- `offset` (table) — 位置偏移
- `rot` (table) — 旋转
- `scale` (table) — 缩放
**返回值**:
- `partName` (string / nil) — 部件名字

---
### `CreateGunInWorld`
**描述**: 在位置上创建枪械掉落物
**参数**:
- `itemid` (number / string) — 道具ID
- `pos` (table) — 掉落物位置{x,y,z}
- `worldId` (number) — 星球ID(默认当前主机所在星球)
**返回值**:
- `id` (number / nil) — 对象ID

---
### `CreateItemInstInWorld`
**描述**: 在位置上创建道具掉落物
**参数**:
- `itemid` (number / string) — 道具ID
- `pos` (table) — 掉落物位置{x,y,z}
- `worldId` (number) — 星球ID(默认当前主机所在星球)
**返回值**:
- `id` (number / nil) — 对象ID

---
### `DeleteSubModelPart`
**描述**: 删除一个道具实例的模型子部件
**参数**:
- `instId` (string) — 道具实例id
- `partName` (string) — 子部件名字
**返回值**:
- `bool` (boolean) — 是否成功

---
### `GetArrayCustomData`
**描述**: 获取道具实例的自定义数据Array
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 键
**返回值**:
- `value` (table / nil) — 值

---
### `GetAttr`
**描述**: 获取道具属性
**参数**:
- `itemid` (number / string) — 道具ID
- `attr` (number) — 属性类型枚举(ItemAttr) ItemAttr
**返回值**:
- `num` (number) — 属性值

---
### `GetBoolCustomData`
**描述**: 获取道具实例的自定义数据bool
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 键
**返回值**:
- `value` (bool / nil) — 值

---
### `GetCraftIDNum`
**描述**: 获取道具配方数量
**参数**:
- `itemid` (number / string) — 道具ID
**返回值**:
- `num` (number) — 配方数量

---
### `GetCraftMaterialAndNum`
**描述**: 获取道具配方材料与数量
**参数**:
- `itemid` (number / string) — 道具ID
**返回值**:
- `obj` (table) — 原料信息{{itemid
- `` — num}}

---
### `GetCustomGunAttr`
**描述**: 获取自定义枪械属性
**参数**:
- `itemid` (number / string) — 道具ID
- `attrname` (string) — 属性名(GunAttr) GunAttr
**返回值**:
- `obj` (any属性值)

---
### `GetEquipItemGridID`
**描述**: 获取装备道具装备栏网格id
**参数**:
- `itemid` (number / string) — 装备道具ID
**返回值**:
- `num` (number) — 装备栏位置 BackpackBeginIndex.Equip + (EquipSlotType)

---
### `GetFacade`
**描述**: 获取道具类型外观
**参数**:
- `itemid` (number / string) — 道具类型ID或道具预制ID
**返回值**:
- `name` (string) — 道具类型外观

---
### `GetGridAttr`
**描述**: 获取掉落物或者投掷物的格子属性
**参数**:
- `objid` (number) — 对象ID
- `attr` (number) — 属性枚举(GridAttr) GridAttr
**返回值**:
- `num` (number / nil) — 属性值

---
### `GetGunAttribute`
**描述**: 获取枪械道具实例的属性
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 属性的枚举(GunAttr) GunAttr
**返回值**:
- `value` (number / string) — / bool / nil 值

---
### `GetGunPrefabAttribute`
**描述**: 获取枪预制的属性
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 属性的枚举(GunAttr) GunAttr
**返回值**:
- `value` (number / string) — / bool / nil 值

---
### `GetItemDesc`
**描述**: 获取道具描述
**参数**:
- `itemid` (number / string) — 道具ID
**返回值**:
- `name` (string) — 道具描述

---
### `GetItemIdByInstanceId`
**描述**: 根据道具实例ID获取道具ID
**参数**:
- `instId` (string) — 道具实例id
**返回值**:
- `itemId` (number / string) — / nil 道具id

---
### `GetItemInstFacade`
**描述**: 获取具有道具实例ID的道具外观
**参数**:
- `instId` (string) — 道具实例ID
**返回值**:
- `name` (string / nil) — 道具实例外观

---
### `GetItemName`
**描述**: 获取道具名称
**参数**:
- `itemid` (number / string) — 道具ID
**返回值**:
- `name` (string) — 道具名称

---
### `GetNumberCustomData`
**描述**: 获取道具实例的自定义数据number
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 键
**返回值**:
- `value` (number / nil) — 值

---
### `GetObjCustomData`
**描述**: 获取道具实例的自定义数据Object
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 键
**返回值**:
- `value` (table / nil) — 值

---
### `GetStringCustomData`
**描述**: 获取道具实例的自定义数据string
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 键
**返回值**:
- `value` (string / nil) — 值

---
### `GetTags`
**描述**: 获取道具定义中的标签组
**参数**:
- `itemid` (number / string) — 道具定义ID或道具预制ID
**返回值**:
- `obj` (table / nil) — 标签组

---
### `ModifyGunAttribute`
**描述**: 修改枪械道具实例的属性
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 属性的枚举(GunAttr) GunAttr
- `value` (number / string) — / bool 值
**返回值**:
- `bool` (boolean) — 是否成功

---
### `RandomItemID`
**描述**: 随机获取道具ID
**返回值**:
- `num` (number) — 道具ID

---
### `RandomProjectileID`
**描述**: 随机获取投掷物ID
**返回值**:
- `num` (number) — 道具ID

---
### `ReplaceSubModelPart`
**描述**: 修改一个道具实例的模型子部件
**参数**:
- `instId` (string) — 道具实例id
- `partName` (string) — 子部件名字
- `boneName` (string) — 挂点
- `modelStr` (string) — 模型
- `offset` (table) — 位置偏移
- `rot` (table) — 旋转
- `scale` (table) — 缩放
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetArrayCustomData`
**描述**: 设置道具实例的自定义数据Array
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 键
- `value` (table) — 数组
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetBoolCustomData`
**描述**: 设置道具实例的自定义数据bool
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 键
- `value` (bool值)
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetNumberCustomData`
**描述**: 设置道具实例的自定义数据number
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 键
- `value` (number) — 值
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetObjCustomData`
**描述**: 设置道具实例的自定义数据Object
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 键
- `value` (table) — 值
**返回值**:
- `bool` (boolean) — 是否成功

---
### `SetStringCustomData`
**描述**: 设置道具实例的自定义数据string
**参数**:
- `instId` (string) — 道具实例id
- `key` (string) — 键
- `value` (string) — 值
**返回值**:
- `bool` (boolean) — 是否成功

---

## Map
### `ClearData`
**描述**: 清空表数据
**参数**:
- `varId` (string / userdata) — 变量表或临时Map
- `playerId` (number) — 玩家Uin
**返回值**:
- `ret` (bool / nil) — 是否成功

---
### `GetIndexValueAndBlock`
**描述**: 阻塞获取排行榜指定名次
**参数**:
- `call_back` (function内部结果回调)
- `varId` (string / userdata) — 排行榜变量或临时Map
- `playerId` (number) — 玩家Uin
- `index` (number) — 名次索引
- `ascending` (bool是否升序)
**返回值**:
- `ret` (bool是否已投递处理)

---
### `GetIndexValueAndCallback`
**描述**: 回调获取排行榜指定名次
**参数**:
- `varId` (string / userdata) — 排行榜变量或临时Map
- `playerId` (number) — 玩家Uin
- `index` (number) — 名次索引
- `ascending` (bool是否升序)
- `callback` (function完成回调)
**返回值**:
- `ret` (bool是否成功发起调用)

---
### `GetNumValuesAndCallback`
**描述**: 回调获取排行榜前N条
**参数**:
- `varId` (string / userdata) — 排行榜变量或临时Map
- `playerId` (number) — 玩家Uin
- `num` (number) — 条数
- `ascending` (bool是否升序)
- `callback` (function完成回调)
**返回值**:
- `ret` (bool是否成功发起调用)

---
### `GetRangeIndexsAndCallback`
**描述**: 回调获取排行榜名次区间
**参数**:
- `varId` (string / userdata) — 排行榜变量或临时Map
- `playerId` (number) — 玩家Uin
- `min` (number) — 最前名次
- `max` (number) — 最后名次
- `ascending` (bool是否升序)
- `callback` (function完成回调)
**返回值**:
- `ret` (bool是否成功发起调用)

---
### `GetRangeValuesAndCallback`
**描述**: 回调获取排行榜分数区间
**参数**:
- `varId` (string / userdata) — 排行榜变量或临时Map
- `playerId` (number) — 玩家Uin
- `min` (number) — 最小分数
- `max` (number) — 最大分数
- `ascending` (bool是否升序)
- `pagesize` (number) — 单页条数
- `callback` (function完成回调)
**返回值**:
- `ret` (bool是否成功发起调用)

---
### `GetValueAndBlock`
**描述**: 阻塞获取KV数据
**参数**:
- `call_back` (function内部结果回调)
- `varId` (string / userdata) — 变量表或临时Map
- `playerId` (number) — 玩家Uin
- `key` (string / number) — 键
**返回值**:
- `ret` (bool是否已投递处理)

---
### `GetValueAndCallBack`
**描述**: 回调获取KV数据
**参数**:
- `varId` (string / userdata) — 变量表或临时Map
- `playerId` (number) — 玩家Uin
- `key` (string / number) — 键
- `callback` (function完成回调)
**返回值**:
- `ret` (bool是否成功发起调用)

---
### `IncreasesRankValueAndBlock`
**描述**: 阻塞增加排行榜分数
**参数**:
- `call_back` (function内部结果回调)
- `varId` (string / userdata) — 排行榜变量或临时Map
- `playerId` (number) — 玩家Uin
- `key` (string / number) — 键
- `value` (number) — 增量
- `extendvalue` (string / number) — / boolean / nil 扩展信息
**返回值**:
- `ret` (bool是否已投递处理)

---
### `IncreasesRankValueAndCallback`
**描述**: 回调增加排行榜分数
**参数**:
- `varId` (string / userdata) — 排行榜变量或临时Map
- `playerId` (number) — 玩家Uin
- `key` (string / number) — 键
- `value` (number) — 增量
- `extendvalue` (string / number) — / boolean / nil 扩展信息
- `call_back` (function完成回调)
**返回值**:
- `ret` (bool是否已投递处理)

---
### `RemoveValueAndBlock`
**描述**: 阻塞删除KV数据
**参数**:
- `call_back` (function内部结果回调)
- `varId` (string / userdata) — 变量表或临时Map
- `playerId` (number) — 玩家Uin
- `key` (string / number) — 键
**返回值**:
- `ret` (bool是否已投递处理)

---
### `RemoveValueAndCallBack`
**描述**: 回调删除KV数据
**参数**:
- `varId` (string / userdata) — 变量表或临时Map
- `playerId` (number) — 玩家Uin
- `key` (string / number) — 键
- `callback` (function完成回调)
**返回值**:
- `ret` (bool是否成功发起调用)

---
### `SetRankValueAndBlock`
**描述**: 阻塞设置排行榜分数
**参数**:
- `call_back` (function内部结果回调)
- `varId` (string / userdata) — 排行榜变量或临时Map
- `playerId` (number) — 玩家Uin
- `key` (string / number) — 键
- `value` (number) — 分数
- `extendvalue` (string / number) — / boolean / nil 扩展信息（仅更新不删，删请用Remove接口）
**返回值**:
- `ret` (bool是否已投递处理)

---
### `SetValueAndBlock`
**描述**: 阻塞设置KV数据
**参数**:
- `call_back` (function内部结果回调)
- `varId` (string / userdata) — 变量表或临时Map
- `playerId` (number) — 玩家Uin
- `key` (string / number) — 键
- `value` (string / number) — / boolean 值
**返回值**:
- `ret` (bool是否已投递处理)

---
### `SetValueAndCallBack`
**描述**: 回调设置KV数据
**参数**:
- `varId` (string) — 变量表或排行榜ID
- `playerId` (number) — 玩家Uin
- `key` (string / number) — 键（数字会转字符串）
- `value` (string / number) — / boolean 值
- `callback` (function完成回调)
**返回值**:
- `ret` (bool是否成功发起调用)

---
### `UpdateValueAndCallback`
**描述**: 回调更新KV数据
**参数**:
- `varId` (string) — 变量表ID
- `playerId` (number) — 玩家Uin
- `key` (string / number) — 键
- `callback` (function完成回调)
**返回值**:
- `ret` (bool是否成功发起调用)

---

## Mod
### `GetCfgIdByAssetId`
**描述**: 通过资源id获取defid
**参数**:
- `assetId` (string) — 资源id
**返回值**:
- `cfgId` (number) — defid

---

## Monster
### `CanSee`
**描述**: 怪物是否可见目标
**参数**:
- `objid` (number) — 怪物对象ID
- `targetObjid` (number) — 目标对象ID
**返回值**:
- `result` (bool是否可见)

---
### `ChangeAI`
**描述**: 切换AI行为树
**参数**:
- `objid` (number) — 生物objid
- `treeid` (string) — 行为树ID
**返回值**:
- `ret` (bool是否成功)

---
### `GetActorID`
**描述**: 获取生物类型ID
**参数**:
- `objid` (number) — 生物objid
**返回值**:
- `actorid` (number / nil) — 生物defId

---
### `GetActorName`
**描述**: 获取生物类型名称
**参数**:
- `objid` (number) — 生物objid
**返回值**:
- `name` (string / nil) — 生物类型名称

---
### `GetDropItemInfo`
**描述**: 获取生物的掉落物信息
**参数**:
- `actorid` (number / string) — 生物类型id或生物预制ID
**返回值**:
- `ret` (table / nil) — 掉落物信息数组（{itemId,num,odds}）

---
### `GetFacade`
**描述**: 获取生物外观
**参数**:
- `monsterid` (number / string) — 生物类型id或生物预制ID
**返回值**:
- `model` (string / nil) — 外观名

---
### `GetMonsterDefLevelExp`
**描述**: 获取击杀掉落经验
**参数**:
- `actorid` (number / string) — 生物类型id或生物预制ID
**返回值**:
- `exp` (number / nil) — 掉落经验

---
### `GetMonsterDefName`
**描述**: 获取生物名称
**参数**:
- `actorid` (number / string) — 生物类型ID或生物预制ID
**返回值**:
- `name` (string / nil) — 生物类型名字

---
### `GetTags`
**描述**: 获取生物标签组
**参数**:
- `actorid` (number / string) — 生物类型id或生物预制ID
**返回值**:
- `ret` (table / nil) — 标签组

---
### `GetTamedOwnerID`
**描述**: 获取驯养主ID
**参数**:
- `objid` (number) — 生物对象ID
**返回值**:
- `ownerId` (number / nil) — 驯养主对象ID

---
### `RandomActorID`
**描述**: 随机获取生物类型ID
**返回值**:
- `ret` (number / nil) — 随机生物类型ID

---
### `ReplaceActor`
**描述**: 替换生物
**参数**:
- `objidSrc` (number) — 源对象ID
- `actorid` (number / string) — 目标生物defId或资源id
- `replacehp` (bool / nil) — 是否替换血量
**返回值**:
- `ret` (number / nil) — 替换后的生物objid

---
### `SetMonsterDefLevelExp`
**描述**: 设置击杀掉落经验
**参数**:
- `actorid` (number / string) — 生物类型id或生物预制ID
- `levelExp` (number) — 掉落经验
**返回值**:
- `ret` (bool是否成功)

---
### `SetTameTarget`
**描述**: 使生物被指定对象驯服
**参数**:
- `objidA` (number) — 生物对象ID
- `objidB` (number) — 玩家对象ID
**返回值**:
- `ret` (bool是否成功)

---

## Player
### `ChangPlayerMoveType`
**描述**: 切换移动方式
**参数**:
- `uin` (number) — 玩家Uin
- `moveType` (number) — 移动方式枚举(MoveType) MoveType
**返回值**:
- `ret` (boolean) — 是否成功

---
### `ChangeViewMode`
**描述**: 切换视角模式
**参数**:
- `objid` (number) — 玩家Uin
- `viewmode` (number) — 视角枚举(ViewPortType) ViewPortType
- `islock` (bool是否锁定)
**返回值**:
- `ret` (boolean) — 是否成功

---
### `ClearMotion`
**描述**: 清空运动趋势
**参数**:
- `uin` (number) — 玩家Uin
**返回值**:
- `ret` (boolean) — 是否成功

---
### `ForceOpenBoxUI`
**描述**: 强制打开箱子UI
**参数**:
- `objid` (number) — 玩家Uin
- `itemid` (number) — 枚举(WorkStage) Stage
**返回值**:
- `ret` (boolean) — 是否成功

---
### `GetAimDir`
**描述**: 获取准心方向
**参数**:
- `objid` (number) — 玩家Uin
**返回值**:
- `dir` (table / nil) — 单位方向向量{x=单位方向x,y=单位方向y,z=单位方向z}

---
### `GetAimPos`
**描述**: 获取准心位置
**参数**:
- `objid` (number) — 玩家Uin
**返回值**:
- `x` (number / nil) — 坐标x
- `y` (number / nil) — 坐标y
- `z` (number / nil) — 坐标z

---
### `GetClientInfo`
**描述**: 获取客机类型
**参数**:
- `uin` (number / nil) — 玩家Uin（兼容参数，当前未使用）
**返回值**:
- `ret` (number) — 设备类型（DeviceType：1 PC 2 Android 3 iOS）

---
### `GetCurToolID`
**描述**: 获取手持道具ID
**参数**:
- `objid` (number) — 玩家Uin
**返回值**:
- `ret` (number / string) — / nil 道具ID

---
### `GetFirstInviter`
**描述**: 获取首次邀请人
**参数**:
- `call_back` (function内部回调(缺省参数))
- `objid` (number) — 被邀请玩家Uin
**返回值**:
- `uin` (number / nil) — 邀请人玩家Uin（失败时回调错误码number）

---
### `GetFriendList`
**描述**: 获取好友列表
**参数**:
- `uin` (number) — 玩家Uin
- `index` (number) — 起始索引
- `size` (number) — 获取数量
**返回值**:
- `totalnum` (number) — 好友总人数
- `friendlist` (table) — 好友列表{..,{name = string,uin = number,headframe = string,live = bool},...},...}

---
### `GetHostUin`
**描述**: 获取房主Uin
**返回值**:
- `ret` (number / nil) — 玩家Uin

---
### `GetMiniCurrency`
**描述**: 获取迷你币数量
**参数**:
- `objid` (number) — 玩家Uin
- `itype` (number) — 币种类型(MiniCurrency) MiniCurrency
**返回值**:
- `num` (number) — 数量

---
### `GetMiniVipLevel`
**描述**: 获取VIP等级
**参数**:
- `playerid` (number) — 玩家Uin
**返回值**:
- `ret` (boolean) — 是否成功上报

---
### `GetNickname`
**描述**: 获取玩家昵称
**参数**:
- `objid` (number) — 玩家Uin
**返回值**:
- `name` (string / nil) — 玩家昵称

---
### `GetPlayerCostStatic`
**描述**: 获取玩家消费统计
**参数**:
- `call_back` (function内部回调(缺省参数))
- `playerid` (number) — 玩家Uin
- `tbegin` (number) — 开始时间
- `tend` (number) — 结束时间
- `costtype` (number) — 查询类型（MiniCurrency） MiniCurrency
**返回值**:
- `icount` (number) — 消费数量（-1表示失败）

---
### `GetRayOriginPos`
**描述**: 获取射线起点位置
**参数**:
- `objid` (number) — 玩家Uin
**返回值**:
- `x` (number / nil) — 坐标x
- `y` (number / nil) — 坐标y
- `z` (number / nil) — 坐标z

---
### `GetRentCloudServerOwner`
**描述**: 获取云房间房主
**返回值**:
- `uin` (number / nil) — 房主玩家Uin

---
### `GetRevivePoint`
**描述**: 获取复活点
**参数**:
- `uin` (number) — 玩家Uin
**返回值**:
- `x` (number / nil) — 方块x
- `y` (number / nil) — 方块y
- `z` (number / nil) — 方块z

---
### `GetScreenSpacePos`
**描述**: 获取屏幕坐标
**参数**:
- `playerid` (number) — 玩家Uin
- `x` (number) — 坐标x(cm)
- `y` (number) — 坐标y(cm)
- `z` (number) — 坐标z(cm)

---
### `GetScreenSpacePosV2`
**描述**: 获取屏幕坐标V2
**参数**:
- `playerid` (number) — 玩家Uin
- `x` (number) — 方块坐标x
- `y` (number) — 方块坐标y
- `z` (number) — 方块坐标z

---
### `GetShotcutIndex`
**描述**: 获取当前快捷栏索引（索引从1开始）
**参数**:
- `objid` (number) — 玩家Uin
**返回值**:
- `ret` (number / nil) — 索引值

---
### `GetViewMode`
**描述**: 获取视角模式
**参数**:
- `uin` (number) — 玩家Uin
**返回值**:
- `ret` (number / nil) — 视角模式(ViewPortType)

---
### `HasFriend`
**描述**: 是否好友
**参数**:
- `playerid` (number) — 玩家Uin
- `friendid` (number) — 目标玩家Uin
**返回值**:
- `ret` (boolean) — 是否成功上报

---
### `HideUIView`
**描述**: 隐藏UI界面
**参数**:
- `objid` (number) — 玩家Uin
- `uiname` (number) — 自定义UIID
- `effectid` (number / nil) — 动作ID(可缺省)
- `time` (number / nil) — 动画时间(可缺省)
**返回值**:
- `ret` (boolean) — 是否成功

---
### `IsEquipByResID`
**描述**: 是否装备指定装备
**参数**:
- `objid` (number) — 玩家Uin
- `itemid` (number / string) — 道具类型或资源id
**返回值**:
- `ret` (boolean) — 是否已装备

---
### `ItemSkillCDDone`
**描述**: 道具技能结束冷却
**参数**:
- `objid` (number) — 玩家Uin
- `itemid` (number / string) — 道具ID或资源ID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `ItemSkillCDEnter`
**描述**: 道具技能进入冷却
**参数**:
- `objid` (number) — 玩家Uin
- `itemid` (number / string) — 道具ID或资源ID
- `cd` (number / nil) — 冷却时长
**返回值**:
- `ret` (boolean) — 是否成功

---
### `NotifyGameInfo2Self`
**描述**: 显示飘窗文字
**参数**:
- `objid` (number) — 玩家Uin
- `info` (string) — 文本内容
**返回值**:
- `ret` (boolean) — 是否成功

---
### `OpenBoxByPos`
**描述**: 打开箱子
**参数**:
- `objid` (number) — 玩家Uin
- `x` (number / table) — 方块x坐标或坐标table
- `y` (number / nil) — 方块y坐标
- `z` (number / nil) — 方块z坐标
**返回值**:
- `ret` (boolean) — 是否成功

---
### `OpenDevGoodsBuyDetailedDialog`
**描述**: 打开开发者商品详情页
**参数**:
- `objid` (number) — 玩家Uin
- `devGoodsId` (number) — 商品ID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `OpenDevGoodsBuyDialog`
**描述**: 打开开发者商品购买弹框
**参数**:
- `objid` (number) — 玩家Uin
- `devGoodsId` (number) — 商品ID
- `customDesc` (string) — 自定义商品描述
**返回值**:
- `ret` (boolean) — 是否成功

---
### `OpenDevGoodsPage`
**描述**: 打开开发者商店一级页面
**参数**:
- `playerid` (number) — 玩家Uin
- `pagetype` (number) — 页面枚举值(MiniShopPage) MiniShopPage
- `pagetitle` (string) — 页面标题
**返回值**:
- `ret` (boolean) — 是否成功

---
### `OpenDevStore`
**描述**: 打开开发者商店
**参数**:
- `objid` (number) — 玩家Uin
**返回值**:
- `ret` (boolean) — 是否成功

---
### `OpenDevStoreTab`
**描述**: 打开开发者商店二级分类
**参数**:
- `objid` (number) — 玩家Uin
- `page` (number) — 分类页码
- `name` (string) — 分类名称
**返回值**:
- `ret` (boolean) — 是否成功

---
### `OpenInnerView`
**描述**: 打开/关闭游戏内弹窗
**参数**:
- `uin` (number) — 玩家Uin
- `iview` (number) — 弹窗类型枚举(InnerPopUpview) InnerPopUpview
- `bopen` (bool是否打开)
- `data` (any / nil) — 弹窗附加数据（如储物箱需传入位置）
**返回值**:
- `ret` (boolean) — 是否成功

---
### `OpenUIView`
**描述**: 打开UI界面
**参数**:
- `objid` (number) — 玩家Uin
- `uiname` (number) — 自定义UIID
- `effectid` (number / nil) — 动作ID(可缺省)
- `time` (number / nil) — 动画时间(可缺省)
**返回值**:
- `ret` (boolean) — 是否成功

---
### `PauseMusic`
**描述**: 暂停/恢复背景音乐
**参数**:
- `objid` (number) — 玩家Uin
- `musicId` (string) — 声音ID
- `pause` (booltrue暂停/false恢复)
**返回值**:
- `ret` (boolean) — 是否成功

---
### `PlayAdvertising`
**描述**: 播放广告
**参数**:
- `objid` (number) — 玩家Uin
- `adname` (string) — 广告名称
**返回值**:
- `code` (number) — 执行结果(ErrorCode) ErrorCode
- `objid` (number) — 玩家Uin
- `adname` (string) — 广告名称

---
### `PlayMusic`
**描述**: 播放背景音乐2D
**参数**:
- `objid` (number) — 玩家Uin
- `musicId` (string) — 声音ID
- `volume` (number) — 音量
- `pitch` (number) — 音调
- `isLoop` (bool是否循环)
**返回值**:
- `ret` (boolean) — 是否成功

---
### `RemovePlayer`
**描述**: 将玩家移出本局
**参数**:
- `objid` (number) — 玩家Uin
**返回值**:
- `ret` (boolean) — 是否成功

---
### `ResetCameraAttr`
**描述**: 重置摄像机
**参数**:
- `playerid` (number) — 玩家Uin
**返回值**:
- `ret` (boolean) — 是否成功

---
### `ReviveToPos`
**描述**: 玩家在指定位置复活
**参数**:
- `objid` (number) — 玩家Uin
- `x` (number / table) — 方块坐标x或坐标表{x=方块坐标x,y=方块坐标y,z=方块坐标z}
- `y` (number / nil) — 方块坐标y
- `z` (number / nil) — 方块坐标z
**返回值**:
- `ret` (boolean) — 是否成功

---
### `RotateCamera`
**描述**: 旋转摄像机角度
**参数**:
- `objid` (number) — 玩家Uin
- `yaw` (number) — 视角偏航角
- `pitch` (number) — 视角俯仰角
**返回值**:
- `ret` (boolean) — 是否成功

---
### `RotateCameraToActor`
**描述**: 旋转摄像机朝向目标
**参数**:
- `objid` (number) — 玩家Uin
- `targetid` (number) — 目标对象objid
**返回值**:
- `ret` (boolean) — 是否成功

---
### `RotateMainModel`
**描述**: 旋转玩家模型
**参数**:
- `uin` (number) — 玩家Uin
- `yaw` (number) — 水平角
- `pitch` (number) — 俯仰角
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SendFriendApply`
**描述**: 发送好友申请
**参数**:
- `playerid` (number) — 玩家Uin
- `uin2` (number) — 目标玩家Uin
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetCameraAttrState`
**描述**: 设置摄像机属性开关
**参数**:
- `playerid` (number) — 玩家Uin
- `attr` (number) — 摄像机属性(CameraModel) CameraModel
- `enable` (bool是否启用)
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetCameraFovTransformBy`
**描述**: 摄像机按偏移调整视野
**参数**:
- `playerid` (number) — 玩家Uin
- `fov` (number) — 相对当前FOV的增减量（非目标FOV）
- `animid` (number) — 缓动枚举(Easing) Easing
- `time` (number) — 动画时长
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetCameraFovTransformTo`
**描述**: 摄像机FOV到值
**参数**:
- `playerid` (number) — 玩家Uin
- `fov` (number) — FOV值
- `animid` (number) — 缓动枚举(Easing) Easing
- `time` (number) — 动画时长
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetCameraMountObj`
**描述**: 摄像机挂载对象
**参数**:
- `playerid` (number) — 玩家Uin
- `objid` (number) — 挂载对象ID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetCameraMountPos`
**描述**: 摄像机挂载位置
**参数**:
- `playerid` (number) — 玩家Uin
- `pos` (table) — 挂载位置坐标
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetCameraPosTransformBy`
**描述**: 摄像机按偏移移动
**参数**:
- `playerid` (number) — 玩家Uin
- `vec` (table) — 相对当前位置的偏移量
- `animid` (number) — 缓动枚举(Easing) Easing
- `time` (number) — 动画时长
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetCameraPosTransformTo`
**描述**: 摄像机移动到位置
**参数**:
- `playerid` (number) — 玩家Uin
- `vec` (table) — 位置坐标（单位：方块）
- `animid` (number) — 缓动枚举(Easing) Easing
- `time` (number) — 动画时长
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetCameraRotMode`
**描述**: 设置摄像机旋转模式
**参数**:
- `playerid` (number) — 玩家Uin
- `attr` (number) — 摄像机旋转模式(CameraRotate) CameraRotate
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetCameraRotTransformBy`
**描述**: 摄像机相对旋转
**参数**:
- `playerid` (number) — 玩家Uin
- `vec` (table) — 相对角度
- `animid` (number) — 缓动枚举(Easing) Easing
- `time` (number) — 动画时长
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetCameraRotTransformTo`
**描述**: 摄像机旋转到角度
**参数**:
- `playerid` (number) — 玩家Uin
- `vec` (table) — 角度坐标
- `animid` (number) — 缓动枚举(Easing) Easing
- `time` (number) — 动画时长
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetGameResults`
**描述**: 设置对局结果
**参数**:
- `objid` (number) — 玩家Uin
- `result` (number) — 游戏结果（TeamResults） TeamResults
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetGameWin`
**描述**: 设置玩家胜利
**参数**:
- `objid` (number) — 玩家Uin
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetGunActionState`
**描述**: 设置枪械动作开关
**参数**:
- `objid` (number) — 玩家Uin
- `action` (number) — 枪械动作枚举(GunActionBan) GunActionBan
- `switch` (bool是否开启)
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetItemAttAction`
**描述**: 设置道具能力开关
**参数**:
- `objid` (number) — 玩家Uin
- `itemid` (number / string) — 道具ID或资源ID
- `atttype` (number) — 能力枚举(ItemAbility) ItemAbility
- `switch` (bool是否开启)
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetMobileVibrate`
**描述**: 手机震动
**参数**:
- `playerid` (number) — 玩家Uin
- `time` (number) — 震动时长(ms)
- `amplitude` (number) — 震动强度(1~255)
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetRevivePoint`
**描述**: 设置玩家复活点
**参数**:
- `objid` (number) — 玩家Uin
- `x` (number) — 方块坐标x
- `y` (number) — 方块坐标y
- `z` (number) — 方块坐标z
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetSettingAbility`
**描述**: 设置游戏设置权限
**参数**:
- `playerid` (number) — 玩家Uin
- `itype` (number) — 设置项(GameSetting) GameSetting
- `enable` (bool是否允许修改)
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetSettingEnable`
**描述**: 设置游戏开关
**参数**:
- `playerid` (number) — 玩家Uin
- `itype` (number) — 设置项(GameSetting) GameSetting
- `enable` (bool是否开启)
**返回值**:
- `ret` (boolean) — 是否生效

---
### `SetShotcutIndex`
**描述**: 设置当前快捷栏索引
**参数**:
- `objid` (number) — 玩家Uin
- `index` (number) — 快捷栏索引（1~8）
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetSkillCD`
**描述**: 设置技能CD
**参数**:
- `objid` (number) — 玩家Uin
- `itemid` (number / string) — 道具类型或资源id
- `cd` (number) — 冷却时间
**返回值**:
- `ret` (boolean) — 是否成功

---
### `ShakeCamera`
**描述**: 抖动镜头
**参数**:
- `objid` (number) — 玩家Uin
- `duration` (number) — 持续时间
- `power` (number) — 强度（1~1000）
**返回值**:
- `ret` (boolean) — 是否成功

---
### `StandReportEvent`
**描述**: 上报埋点事件
**参数**:
- `playerid` (number) — 玩家Uin
- `eventstr` (string) — 事件名称
**返回值**:
- `ret` (boolean) — 是否成功

---
### `StopMusic`
**描述**: 停止背景音乐2D
**参数**:
- `objid` (number) — 玩家Uin
- `musicId` (string) — 声音ID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `StopShakeCamera`
**描述**: 停止抖动镜头
**参数**:
- `objid` (number) — 玩家Uin
**返回值**:
- `ret` (boolean) — 是否成功

---

## Table
### `Clear`
**描述**: 清空表格
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
**返回值**:
- `ret` (boolean) — 是否成功

---
### `GetAllValue`
**描述**: 获取整张表
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
**返回值**:
- `value` (table / nil) — 整张表数据

---
### `GetColIndex`
**描述**: 获取列索引
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
- `key` (any列名或列) — key
**返回值**:
- `ret` (number / nil) — 列索引

---
### `GetCols`
**描述**: 获取列数
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
**返回值**:
- `ret` (number / nil) — 列数

---
### `GetRowIndex`
**描述**: 查找行号
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
- `col` (number / string) — 列号或列名
- `value` (any要匹配的值)
- `cmp` (function / nil) — 比较函数(可为nil，function(a,value) return a == value end)，默认判断值相等 ction
**返回值**:
- `ret` (number / nil) — 行号

---
### `GetRowIndexs`
**描述**: 查找全部行号
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
- `col` (number / string) — 列号或列名
- `value` (any要匹配的值)
- `cmp` (function / nil) — 比较函数(可为nil，function(a,value) return a == value end)，默认判断值相等 ction
**返回值**:
- `ret` (table / nil) — 行号列表

---
### `GetRows`
**描述**: 获取行数
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
**返回值**:
- `ret` (number / nil) — 行数

---
### `GetTableColKeys`
**描述**: 获取列名列表
**参数**:
- `varId` (string) — 表ID
**返回值**:
- `ret` (table / nil) — 列名列表，失败为 nil

---
### `GetValue`
**描述**: 获取表格数据
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
- `row` (number) — 行号
- `col` (number / string) — / nil 列号或列名（可省略）
**返回值**:
- `value` (any / nil) — 单元格值或整行表

---
### `GetValuesByCol`
**描述**: 获取指定列的所有行数据
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
- `col` (number / string) — 列号或列名
**返回值**:
- `ret` (table / nil) — 该列所有行数据

---
### `InsertValue`
**描述**: 在末尾插入一行数据
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
- `...:any列值依次传入（中间不可传` — nil）
**返回值**:
- `ret` (boolean) — 是否成功

---
### `InsertValueByRow`
**描述**: 在指定行插入一行数据
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
- `value` (table) — 列值
- `row` (number / nil) — 插入位置（nil 表示插到末尾）
**返回值**:
- `ret` (boolean) — 是否成功

---
### `RemoveRow`
**描述**: 删除行
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
- `row` (number / table) — 行号或行号列表
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetValue`
**描述**: 设置单元格或整行数据
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
- `row` (number / table) — 行号或行号数组
- `col` (number / string) — / nil 列号或列名（可省略）
- `value` (any新值或整行表)
**返回值**:
- `ret` (boolean / nil) — 是否成功

---
### `UpdateAllValue`
**描述**: 更新整张表
**参数**:
- `varId` (string) — 表ID
- `playerId` (number / nil) — 玩家Uin（全局表传nil）
- `value` (table) — 新表数据
**返回值**:
- `ret` (boolean / nil) — 是否成功

---

## Timer
### `ChangeTimerTime`
**描述**: 设置计时器时间
**参数**:
- `id` (number) — 计时器ID
- `curtime` (number) — 当前秒数
**返回值**:
- `ret` (boolean) — 是否成功

---
### `CreateTimer`
**描述**: 创建计时器
**参数**:
- `name` (string) — 计时器名称
**返回值**:
- `timerid` (number / nil) — 计时器ID

---
### `DeleteTimer`
**描述**: 删除计时器
**参数**:
- `id` (number) — 计时器ID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `GetTimerTime`
**描述**: 获取计时器时间
**参数**:
- `id` (number) — 计时器ID
**返回值**:
- `runtime` (number / nil) — 当前秒数

---
### `HideTimerWnd`
**描述**: 隐藏计时器窗口
**参数**:
- `playerids` (number / table) — 玩家Uin或Uin数组
**返回值**:
- `ret` (boolean) — 是否成功

---
### `IsExist`
**描述**: 计时器是否存在
**参数**:
- `id` (number) — 计时器ID
**返回值**:
- `ret` (boolean) — 是否存在

---
### `PauseTimer`
**描述**: 暂停计时器
**参数**:
- `id` (number) — 计时器ID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `ResumeTimer`
**描述**: 恢复计时器
**参数**:
- `id` (number) — 计时器ID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `ShowTimerWnd`
**描述**: 显示计时器窗口
**参数**:
- `playerids` (number / table) — 玩家Uin或Uin数组
- `timerid` (number) — 计时器ID
- `title` (string / nil) — 标题
**返回值**:
- `ret` (boolean) — 是否成功

---
### `StartBackwardTimer`
**描述**: 开始倒计时
**参数**:
- `id` (number) — 计时器ID
- `interval` (number) — 起始秒数
- `repeated` (bool / nil) — 是否循环
**返回值**:
- `ret` (boolean) — 是否成功

---
### `StartForwardTimer`
**描述**: 开始正向计时
**参数**:
- `id` (number) — 计时器ID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `StopTimer`
**描述**: 停止计时器
**参数**:
- `id` (number) — 计时器ID
**返回值**:
- `ret` (boolean) — 是否成功

---

## World
### `AddGravity`
**描述**: 增加重力
**参数**:
- `value` (number) — 增加量
**返回值**:
- `ret` (boolean) — 是否成功

---
### `CalcDirectionByAngle`
**描述**: 角度转方向向量
**参数**:
- `yaw` (number) — 水平角(度制)
- `pitch` (number) — 俯仰角(度制)

---
### `CalcDirectionByCoord`
**描述**: 坐标转表
**参数**:
- `x` (number) — 坐标分量x
- `y` (number) — 坐标分量y
- `z` (number) — 坐标分量z

---
### `CalcDirectionByPos2Pos`
**描述**: 两点单位方向
**参数**:
- `pos1` (table) — 位置1{x=number,y=number,z=number}
- `pos2` (table) — 位置2{x=number,y=number,z=number}
**返回值**:
- `ret` (table / nil) — 单位方向{x,y,z}（入参非法返回nil）

---
### `CalcDirectionByYawAngle`
**描述**: 局部方向转世界方向(角度)
**参数**:
- `objid` (number) — 对象ID
- `yaw` (number) — 水平角(度制)
- `pitch` (number) — 俯仰角(度制)
**返回值**:
- `ret` (table / nil) — 世界方向向量{x,y,z}（失败返回nil）

---
### `CalcDirectionByYawDirection`
**描述**: 局部方向转世界方向(向量)
**参数**:
- `objid` (number) — 对象ID
- `vx|vy|vz:` — number 局部方向分量

---
### `CalcDistance`
**描述**: 计算两点距离
**参数**:
- `posSrc` (table:源坐标{x:) — number, y: number, z: number}
- `posDst` (table:目标坐标{x:) — number, y: number, z: number}
**返回值**:
- `ret` (number / nil) — 两点距离（入参非法返回nil）

---
### `CanMobSpawnOnPosXZ`
**描述**: 获取可刷怪的Y坐标
**参数**:
- `x` (number) — x
- `y` (number) — y
- `z` (number) — z
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `posy` (number) — 查到的可刷怪落脚 Y（-1 表示未找到）

---
### `DespawnActor`
**描述**: 移除生物
**参数**:
- `objid` (number) — 对象objID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `FindCanSpawnMobPosList`
**描述**: 查找附近可刷怪位置列表
**参数**:
- `centerX` (number) — 中心x
- `centerY` (number) — 中心y
- `centerZ` (number) — 中心z
- `radius` (number) — 半径
- `includeCenterPos` (bool / nil) — 是否包含中心点
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `posList` (table / nil) — 位置列表

---
### `FindEcosystem`
**描述**: 查找地形位置
**参数**:
- `x|y|z:` — number 查找起点位置坐标
- `biomeType` (number) — 地形类型（BiomeType） BiomeType
- `radius` (number / nil) — 查找半径(单位chunk，默认1，1 chunk=16*16的方块)
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `` — retX|retY|retZ: number / nil 找到的地形位置坐标（失败返回nil）

---
### `FindNearestPlayerByPos`
**描述**: 获取离指定位置最近的玩家
**参数**:
- `posX` (number) — x
- `posY` (number) — y
- `posZ` (number) — z
- `worldId` (number / nil) — 星球ID(默认当前主机星球)
**返回值**:
- `objid` (number / nil) — 玩家ID

---
### `GetAllPlayers`
**描述**: 获取全部玩家对象ID列表
**参数**:
- `alive` (number / nil) — 玩家状态（0阵亡 1存活 -1全部）
**返回值**:
- `list` (table / nil) — 玩家objid数组

---
### `GetBiomeGroup`
**描述**: 获取地形组类型
**参数**:
- `posX|posZ:` — number 位置坐标
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (number / nil) — 地形组类型（WeatherGroup）

---
### `GetBiomeType`
**描述**: 获取地形类型
**参数**:
- `posX|posZ:` — number 位置坐标
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (number / nil) — 地形类型（BiomeType）

---
### `GetDateFromTime`
**描述**: 时间戳转时间字段
**参数**:
- `time` (number) — 时间戳
- `enum` (number) — 枚举值（EventDate） EventDate
**返回值**:
- `ret` (number) — 时间值（入参非法返回0）

---
### `GetDay`
**描述**: 获取天数
**返回值**:
- `ret` (number / nil) — 天数

---
### `GetDirRayDetection`
**描述**: 方向射线检测
**参数**:
- `posbegin` (table) — 起点{x=0,y=0,z=0}
- `dir` (table) — 方向向量{x=0,y=0,z=0}
- `maxlen` (number) — 最大检测距离
- `picktype` (number) — 检测类型(RayDetectType) RayDetectType
- `worldId` (number / nil) — 星球ID
- `ignoreObjs` (table / nil) — 忽略对象ID数组

---
### `GetGameMode`
**描述**: 获取游戏模式
**返回值**:
- `ret` (number / nil) — 游戏模式(WorldType)

---
### `GetGravity`
**描述**: 获取重力
**参数**:
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `value` (number / nil) — 重力值

---
### `GetGroupWeather`
**描述**: 获取天气组天气
**参数**:
- `groupid` (number) — 天气组ID(WeatherGroup)
**返回值**:
- `ret` (number / nil) — 天气值（入参非法返回nil）

---
### `GetHostWorldId`
**描述**: 获取主机星球ID
**返回值**:
- `worldId` (number) — 星球ID

---
### `GetHours`
**描述**: 获取时间（小时）
**返回值**:
- `curHour` (number / nil) — 小时

---
### `GetLightByPos`
**描述**: 获取光照强度
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `worldId` (number / nil) — 星球ID
**返回值**:
- `lv` (number) — 光照强度(0~16)，失败为-1

---
### `GetLocalDate`
**描述**: 获取本地时间字段
**参数**:
- `enum` (number) — 枚举值（EventDate）
**返回值**:
- `ret` (number) — 时间值

---
### `GetLocalDateString`
**描述**: 获取本地时间字符串
**返回值**:
- `ret` (string) — 时间字符串

---
### `GetPlayerTotal`
**描述**: 获取玩家数量
**参数**:
- `alive` (number / nil) — 玩家状态（0阵亡 1存活 -1全部）
**返回值**:
- `ret` (number) — 玩家数量，失败为-1

---
### `GetRayBlock`
**描述**: 射线命中方块
**参数**:
- `srcx|srcy|srcz:` — number 起点坐标
- `face` (number) — 方向/面
- `distance` (number) — 最大检测距离
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (number / string) — / nil 方块ID（可能返回自定义资源ID；未命中返回nil）

---
### `GetRayLength`
**描述**: 计算射线长度
**参数**:
- `srcx|srcy|srcz:` — number 起点坐标
- `dstx|dsty|dstz:` — number 终点坐标
- `distance` (number) — 最大检测距离
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (number / nil) — 射线长度（失败返回nil）

---
### `GetServerDate`
**描述**: 获取服务器时间字段
**参数**:
- `enum` (number) — 枚举值（EventDate）
**返回值**:
- `ret` (number) — 时间值（取不到返回0）

---
### `GetSpawnPoint`
**描述**: 获取世界默认出生点
**返回值**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z

---
### `IsChunkLoaded`
**描述**: 区块是否加载
**参数**:
- `x` (number) — x
- `z` (number) — z
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否已加载

---
### `IsDaytime`
**描述**: 是否白天
**返回值**:
- `ret` (boolean) — 是否白天

---
### `PauseSoundEffectOnPos`
**描述**: 暂停/恢复音效
**参数**:
- `pos` (table) — 位置
- `soundId` (number) — 音效ID（-1表示全部）
- `pause` (boolean) — true暂停 false恢复
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否成功

---
### `PixelMapAddMarker`
**描述**: 地图增加标记
**参数**:
- `uin` (number) — 玩家ID
- `id` (string) — 标记ID
- `params` (table) — 标记参数
**返回值**:
- `ret` (boolean) — 是否添加成功

---
### `PixelMapAddTexture`
**描述**: 增加地图纹理标签
**参数**:
- `uin` (number) — 玩家ID
- `id` (string) — 纹理ID
- `params` (table) — 纹理参数
**返回值**:
- `ret` (boolean) — 是否添加成功

---
### `PixelMapDelMarker`
**描述**: 地图删除标记
**参数**:
- `uin` (number) — 玩家ID
- `id` (string) — 标记ID
**返回值**:
- `ret` (boolean) — 是否删除成功

---
### `PixelMapDelTexture`
**描述**: 地图删除纹理标签
**参数**:
- `uin` (number) — 玩家ID
- `id` (string) — 纹理ID
**返回值**:
- `ret` (boolean) — 是否删除成功

---
### `PixelMapRefreshMarker`
**描述**: 地图刷新标记
**参数**:
- `uin` (number) — 玩家ID
- `id` (string) — 标记ID
- `params` (table) — 标记参数(提供改变的参数即可)
**返回值**:
- `ret` (boolean) — 是否刷新成功

---
### `PixelMapRefreshTexture`
**描述**: 刷新地图纹理标签
**参数**:
- `uin` (number) — 玩家ID
- `id` (string) — 纹理ID
- `params` (table) — 纹理参数(提供改变的参数即可)
**返回值**:
- `ret` (boolean) — 是否刷新成功

---
### `PlayParticle`
**描述**: 播放粒子特效
**参数**:
- `pos` (table) — 位置（米）
- `particleIdArg` (number / string) — / table 特效ID/路径或数组
- `ptimeArg` (number / nil) — 持续秒数
- `offset` (table / nil) — 偏移（米）
- `rot` (table / nil) — 旋转
- `scale` (table / nil) — 缩放
- `worldId` (number / nil) — 星球ID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `PlaySoundEffectOnPos`
**描述**: 播放音效
**参数**:
- `pos` (table) — 位置
- `soundId` (number) — 音效ID
- `volume` (number) — 音量(0~100)
- `pitch` (number / nil) — 音调
- `isLoop` (bool是否循环)
- `worldId` (number / nil) — 星球ID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `RandomParticleEffectID`
**描述**: 随机特效ID
**返回值**:
- `ret` (number / nil) — 特效ID（取不到返回nil）

---
### `RandomSoundID`
**描述**: 随机音效ID
**返回值**:
- `ret` (number / nil) — 音效ID（取不到返回nil）

---
### `RandomWeatherID`
**描述**: 随机天气ID
**返回值**:
- `ret` (number / nil) — 天气ID（取不到返回nil）

---
### `SetGravity`
**描述**: 设置重力
**参数**:
- `value` (number) — 重力值
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetGroupWeather`
**描述**: 设置天气组天气
**参数**:
- `groupid` (number) — 天气组ID(WeatherGroup) WeatherGroup
- `weatherid` (number) — 天气ID(GroupWeatherType) GroupWeatherType
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetHours`
**描述**: 设置时间（小时）
**参数**:
- `time` (number) — 小时（0~24）
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetInnerViewEnable`
**描述**: 设置内置界面启用
**参数**:
- `iview` (number) — 弹窗类型枚举(InnerPopUpview) InnerPopUpview
- `bopen` (boolean) — 启用(true)/禁用(false)
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetLightByPos`
**描述**: 设置方块光照
**参数**:
- `x` (number) — 位置x
- `y` (number) — 位置y
- `z` (number) — 位置z
- `value` (number) — 光照强度(0~15)
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetMidJoin`
**描述**: 设置中途加入开关
**参数**:
- `enable` (boolean) — 是否允许中途加入
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetMobSpawnDensity`
**描述**: 设置生物生成密度
**参数**:
- `mobType` (number) — 生物类型(MobType) MobType
- `density` (number) — 密度(0~2000)
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetParticleTransform`
**描述**: 设置粒子变换
**参数**:
- `pos` (table) — 位置（米）
- `particleIdArg` (number / string) — / table 特效ID/路径或数组
- `offset` (table / nil) — 偏移（米）
- `rot` (table / nil) — 旋转
- `scale` (table / nil) — 缩放
- `worldId` (number / nil) — 星球ID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `SetPlantGrowRate`
**描述**: 设置农作物生长倍率
**参数**:
- `rate` (number) — 时间倍率(>0)
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetSkyBoxAttr`
**描述**: 设置天空盒属性
**参数**:
- `time` (number) — 游戏时间(小时)
- `itype` (number) — 参数类型(SkyboxAttr) SkyboxAttr
- `value` (number) — 参数值(0~100)
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetSkyBoxAttrWithNoTime`
**描述**: 设置天空盒属性(不带时间)
**参数**:
- `itype` (number) — 参数类型(SkyboxAttr) SkyboxAttr
- `value` (number) — 参数值(0~100)
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetSkyBoxColor`
**描述**: 设置天空盒颜色
**参数**:
- `time` (number) — 游戏时间(小时)
- `itype` (number) — 颜色属性枚举(SkyboxColor) SkyboxColor
- `color` (string) — 16进制颜色值(如0xffffff)
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetSkyBoxColorAnim`
**描述**: 设置天空盒颜色(动效)
**参数**:
- `playerid` (number) — 玩家ID
- `itype` (number) — 颜色属性枚举(SkyboxColor) SkyboxColor
- `color` (string) — 16进制颜色值(如0xffffff)
- `animId` (number) — 动画枚举(Easing) Easing
- `animTime` (number) — 动画时间
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetSkyBoxFilter`
**描述**: 设置天空盒滤镜
**参数**:
- `playerid` (number) — 玩家ID
- `itype` (number) — 参数类型(SkyboxFilter) SkyboxFilter
- `value` (number / string) — 参数值(0~100)或16进制颜色值(如0xffffff)
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetSkyBoxFilterAnim`
**描述**: 设置天空盒滤镜(动效)
**参数**:
- `playerid` (number) — 玩家ID
- `itype` (number) — 参数类型(SkyboxFilter) SkyboxFilter
- `value` (number / string) — 参数值(0~100)或颜色值
- `animId` (number) — 动画枚举(Easing) Easing
- `animTime` (number) — 动画时间
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetSkyBoxMaps`
**描述**: 设置天空盒贴图
**参数**:
- `itype` (number) — 贴图类型(SkyboxMap) SkyboxMap
- `url` (string) — 图片链接
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetSkyBoxMapsAnim`
**描述**: 设置天空盒贴图(动效)
**参数**:
- `playerid` (number) — 玩家ID
- `itype` (number) — 贴图类型(SkyboxMap) SkyboxMap
- `url` (string) — 图片链接
- `animId` (number) — 动画枚举(Easing) Easing
- `animTime` (number) — 动画时间
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetSkyBoxSwitch`
**描述**: 设置天空盒开关
**参数**:
- `time` (number) — 游戏时间(小时)
- `itype` (number) — 参数类型(SkyboxSwitch) SkyboxSwitch
- `value` (number) — 开关值(0/1)
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetSkyBoxTemplate`
**描述**: 设置天空盒模板
**参数**:
- `value` (number / string) — 模板值
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetSpawnPoint`
**描述**: 设置出生点
**参数**:
- `x|y|z:` — number 方块坐标
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetTimeVanishingSpeed`
**描述**: 设置时间流逝速度
**参数**:
- `speed` (number) — 时间流逝速度
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SetWorldCreateMobRule`
**描述**: 设置世界生物生成规则
**参数**:
- `cfgs` (table) — 生物规则配置
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SpawnCreature`
**描述**: 生成生物
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `mobid` (number / string) — 生物类型
- `num` (number / nil) — 数量
- `trigger` (bool / nil) — 是否触发事件
- `worldId` (number / nil) — 星球ID
**返回值**:
- `objs` (table / nil) — 生成的生物ID数组

---
### `SpawnProjectile`
**描述**: 生成投掷物
**参数**:
- `objid` (number / nil) — 发射者objid
- `itemid` (number / string) — 道具ID或资源ID
- `x` (number) — 起点x
- `y` (number) — 起点y
- `z` (number) — 起点z
- `dstx` (number) — 目标x
- `dsty` (number) — 目标y
- `dstz` (number) — 目标z
- `speed` (number / nil) — 速度
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `objid` (number / nil) — 投掷物objid

---
### `SpawnProjectileByDir`
**描述**: 按方向生成投掷物
**参数**:
- `objid` (number) — 发射者objid
- `itemid` (number / string) — 道具类型/资源ID
- `x|y|z:` — number 生成位置坐标
- `dirx|diry|dirz:` — number 飞行方向分量
- `speed` (number) — 速度
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (number / nil) — 投掷物ID（失败返回nil）

---
### `StopParticleOnPos`
**描述**: 停止指定位置的粒子特效
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `particleId` (number / string) — 特效ID或路径
- `worldId` (number / nil) — 星球ID
**返回值**:
- `ret` (boolean) — 是否成功

---
### `StopSoundEffectOnPos`
**描述**: 停止指定位置上的音效
**参数**:
- `pos` (table) — 位置
- `soundId` (number) — 音效ID（-1表示全部）
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否成功

---

## WorldContainer
### `AddItemToContainer`
**描述**: 储物箱添加道具(大箱)
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `itemid` (number / string) — 道具类型ID或资源ID
- `num` (number) — 数量
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (number / boolean) — 实际添加数量（失败返回false）

---
### `AddStorageItem`
**描述**: 储物箱添加道具
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `itemid` (number / string) — 道具类型ID或资源ID
- `num` (number) — 数量
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (number / boolean) — / nil 实际添加数量（锁定商品返回false，失败返回nil）

---
### `AddWorldStorageItems`
**描述**: 批量添加储物箱道具
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `itemids` (table) — 道具列表({itemId,itemNum}...)
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (number) — 累计成功添加数量

---
### `CheckStorage`
**描述**: 检测储物箱
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)

---
### `CheckStorageEmptyGrid`
**描述**: 检测储物箱空位
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `itemid` (number / string) — 道具类型ID或资源ID
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否有可用格子

---
### `ClearContainer`
**描述**: 清空容器
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否清空成功

---
### `ClearStorageBox`
**描述**: 清空储物箱
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否清空成功

---
### `GetAllStorageItemInstanceIds`
**描述**: 获取储物箱全部道具实例ID
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (table / nil) — 实例ID字符串数组（失败返回nil）

---
### `GetGridAttr`
**描述**: 获取格子属性
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `gridid` (number:格子ID,attr:number:属性枚举(GridAttr))
- `worldId` (number) — 星球id(默认当前主机所在星球)
**返回值**:
- `ret` (number) — 属性值

---
### `GetStorageItem`
**描述**: 获取储物箱格子道具
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `offset` (number) — 格子索引(从1开始)
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)

---
### `GetStorageItemInstanceId`
**描述**: 获取储物箱道具实例ID
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `offset` (number) — 格子索引(从1开始)
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (string / nil) — 实例ID（无则返回nil）

---
### `RemoveContainerItemByID`
**描述**: 移除储物箱中一定数量道具
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `itemid` (number / string) — 道具类型ID或资源ID
- `num` (number) — 数量
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否移除成功

---
### `RemoveStorageItemByID`
**描述**: 储物箱按类型移除道具
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `itemid` (number / string) — 道具类型ID或资源ID
- `num` (number / nil) — 移除数量
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否执行成功

---
### `RemoveStorageItemByIndex`
**描述**: 储物箱按格子移除道具
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `offset` (number) — 格子索引(从1开始)
- `num` (number / nil) — 移除数量
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否移除成功

---
### `SetStorageItem`
**描述**: 设置储物箱格子道具
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `offset` (number) — 格子索引(从1开始)
- `itemid` (number / string) — 道具类型ID或资源ID
- `num` (number) — 数量
- `worldId` (number / nil) — 星球ID(默认当前主机所在星球)
**返回值**:
- `ret` (boolean) — 是否设置成功

---
### `SwapContainerItem`
**描述**: 交换容器与背包道具
**参数**:
- `x` (number) — 坐标x
- `y` (number) — 坐标y
- `z` (number) — 坐标z
- `grid` (number) — 容器格子索引(从1开始，熔炉为约定槽位)
- `uin` (number) — 玩家objid
- `grid2` (number) — 背包格子索引(从1开始)
**返回值**:
- `ret` (boolean / nil) — 是否成功（坐标无方块等可能返回nil）

---
