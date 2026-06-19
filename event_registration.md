# 📋 《迷你世界》UGC 3.0 事件调用完整手册

> **适用范围**：所有组件脚本的事件监听与调用。  
> **使用说明**：查阅事件时请注意区分全局事件（`TriggerEvent`）与局部事件（`ObjectEvent`），选择正确的注册接口。


## 一、事件类型总览

| 事件分类 | 注册接口 | 适用组件 | 事件枚举 |
| :--- | :--- | :--- | :--- |
| **全局事件（触发器事件）** | `self:AddTriggerEvent` | 世界组件、UI组件、界面组件 | `TriggerEvent.xxx` |
| **局部事件（对象事件）** | `self:AddEvent` | 方块组件、生物组件、玩家组件 | `ObjectEvent.xxx` |


## 二、事件注册规范

### 2.1 基础注册

```lua
-- 全局事件注册
self:AddTriggerEvent(TriggerEvent.事件名, self.回调函数)

-- 局部事件注册
self:AddEvent(ObjectEvent.事件名, self.回调函数)
```

### 2.2 带过滤参数注册（性能优化）

```lua
-- 全局事件过滤（第3参数起）
self:AddTriggerEvent(TriggerEvent.PlayerInputKeyDown, self.OnKey, KeyCode.Q)
self:AddTriggerEvent(TriggerEvent.PlayerAreaIn, self.OnArea, areaId)
self:AddTriggerEvent(TriggerEvent.UIButtonClick, self.OnBtn, elementId)
self:AddTriggerEvent(TriggerEvent.PlayerChangeAttr, self.OnHp, RoleAttr.CurHp)

-- 局部事件过滤（第3参数为优先级传nil，第4参数为过滤值）
-- 注意：中间的 nil 不可省略！
self:AddEvent(ObjectEvent.ObjectChangeAttr, self.OnAttr, nil, RoleAttr.CurHp)
```

### 2.3 nil 参数规则

> **中间的 `nil` 不可省略，末尾的 `nil` 可省略。**

```lua
-- ✅ 正确：中间有过滤值，优先级传 nil
self:AddEvent(ObjectEvent.ObjectChangeAttr, self.OnAttr, nil, RoleAttr.CurHp)

-- ✅ 正确：无过滤值，省略末尾 nil
self:AddEvent(ObjectEvent.BlockClicked, self.OnClick)

-- ❌ 错误：中间 nil 被省略
self:AddEvent(ObjectEvent.ObjectChangeAttr, self.OnAttr, RoleAttr.CurHp)  -- 参数错位！
```


## 三、事件参数获取规范

### 3.1 直接获取（首选）

```lua
function Script:OnEvent(event)
    local objId = event.eventobjid    -- 触发者实例ID
    local targetId = event.toobjid    -- 目标对象实例ID
    local blockId = event.blockid     -- 方块类型ID
    local x, y, z = event.x, event.y, event.z
end
```

### 3.2 CurEventParam 补充获取

> **当直接获取的参数为 `nil` 时，使用 `CurEventParam` 替代。**

```lua
function Script:OnEvent(event)
    local param = event.CurEventParam
    local hurt = param.Hurtlv           -- 伤害值
    local buffId = param.EventBuff      -- 状态效果
    local areaId = param.EventAreaid    -- 区域ID
    local elementId = param.EventElementID  -- UI元件ID
end
```

### 3.3 CurEventParam 完整字段列表

| 字段 | 说明 | 字段 | 说明 |
| :--- | :--- | :--- | :--- |
| `EventTargetPos` | 事件中的位置 | `EventBuff` | 状态效果 |
| `EventTargetEffect` | 特效 | `EventTargetBlock` | 方块类型 |
| `EventShortCutIdx` | 快捷栏 | `EquipItemPos` | 装备栏 |
| `EventElementID` | 元件 | `EventUIID` | 界面 |
| `EventString` | 字符串 | `SelectUIID` | 当前编辑界面 |
| `EventAreaid` | 区域 | `Hurtlv` | 伤害值 |
| `TriggerByPlayer` | 触发玩家 | `EventTargetPlayer` | 目标玩家 |
| `TriggerByCreature` | 触发生物 | `EventTargetCreature` | 目标生物 |
| `Actorid` | 触发生物类型 | `targetactorid` | 目标生物类型 |
| `EventTargetItemID` | 道具类型 | `TriggerByMissile` | 触发投射物 |
| `EventTargetDropItem` | 掉落物 | `Itemnum` | 道具数量 |
| `eventworldid` | 星球 | — | — |

### 3.4 ID 类型区分（极易混淆）

| 参数 | 含义 | ID 类型 |
| :--- | :--- | :--- |
| `event.eventobjid` | 触发事件的对象 | **实例 ID** |
| `event.toobjid` | 事件中的目标对象 | **实例 ID** |
| `event.actorid` | 触发事件的生物类型 | **类型 ID** |
| `event.targetactorid` | 事件中的目标生物类型 | **类型 ID** |
| `event.blockid` | 事件中的方块类型 | **类型 ID** |
| `event.itemid` | 事件中的道具类型 | **类型 ID** |

```lua
-- ❌ 错误：类型ID当作实例ID使用
local actorId = event.actorid  -- 这是类型ID（如3400）
Actor:SetAttr(actorId, RoleAttr.CurHp, 100)  -- 错误！

-- ✅ 正确：实例ID操作具体对象
local objId = event.eventobjid  -- 实例ID
Actor:SetAttr(objId, RoleAttr.CurHp, 100)

-- ✅ 正确：类型ID判断种类
if event.actorid == 3400 then  -- 判断是否为野萌宝
    -- 处理逻辑
end
```


## 四、全局事件完整列表（TriggerEvent）

### 4.1 游戏全局事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.GameStart` | 游戏创建 | 无 | — |
| `TriggerEvent.GameHour` | 游戏时间变化 | `hour`, `second`, `ticks` | — |
| `TriggerEvent.GroupWeatherChanged` | 地形组天气改变 | `weathergroupid` | — |
| `TriggerEvent.MinitimerChange` | 任意计时器改变 | 无 | `timerid` |

### 4.2 玩家全局事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.GameAnyPlayerEnterGame` | 玩家进入游戏 | `eventobjid`（玩家实例） | — |
| `TriggerEvent.GameAnyPlayerLeaveGame` | 玩家离开游戏 | `eventobjid`（玩家实例） | — |
| `TriggerEvent.GameAnyPlayerVictory` | 玩家游戏胜利 | `eventobjid` | — |
| `TriggerEvent.GameAnyPlayerDefeat` | 玩家游戏失败 | `eventobjid` | — |
| `TriggerEvent.PlayerRevive` | 玩家复活 | `eventobjid`, `x,y,z` | — |
| `TriggerEvent.PlayerMoveOneBlockSize` | 玩家移动一格 | `eventobjid`, `x,y,z` | — |
| `TriggerEvent.PlayerSelectShortcut` | 玩家选中快捷栏 | `eventobjid`, `itemid`, `itemnum` | — |
| `TriggerEvent.PlayerInvateFriend` | 玩家邀请好友 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.PlayerNewInputContent` | 玩家发送聊天信息 | `eventobjid`, `content` | — |

### 4.3 玩家交互事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.PlayerClickBlock` | 玩家点击方块 | `eventobjid`, `blockid`（方块类型）, `x,y,z` | — |
| `TriggerEvent.PlayerClickPlayer` | 玩家点击玩家 | `eventobjid`, `toobjid`（玩家实例） | — |
| `TriggerEvent.PlayerClickMob` | 玩家点击生物 | `eventobjid`, `toobjid`（生物实例） | — |
| `TriggerEvent.PlayerClickProjectile` | 玩家点击投掷物 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.PlayerClickDropItem` | 玩家点击掉落物 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.PlayerClickEntity` | 玩家点击实体 | `eventobjid`, `toobjid` | — |

### 4.4 玩家按键事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.PlayerInputKeyClick` | 玩家点击按键 | `eventobjid`, `vkey` | `KeyCode.xxx` |
| `TriggerEvent.PlayerInputKeyDown` | 玩家按下按键 | `eventobjid`, `vkey` | `KeyCode.xxx` |
| `TriggerEvent.PlayerInputKeyUp` | 玩家抬起按键 | `eventobjid`, `vkey` | `KeyCode.xxx` |
| `TriggerEvent.PlayerInputKeyOnPress` | 玩家长按按键 | `eventobjid`, `vkey` | `KeyCode.xxx` |

### 4.5 玩家运动事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.PlayerMotionStateChange` | 玩家进入运动状态 | `eventobjid`, `playermotion` | `RoleMotion.xxx` |
| `TriggerEvent.PlayerMotionStateChangeEnd` | 玩家离开运动状态 | `eventobjid`, `playermotion` | `RoleMotion.xxx` |
| `TriggerEvent.PlayerGunAction` | 玩家持枪状态改变 | `eventobjid`, `gunAction`, `gunState` | `GunState.xxx`, `GunAction.xxx` |

### 4.6 玩家道具事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.PlayerAddItem` | 玩家获得道具 | `eventobjid`, `itemid`, `itemnum` | — |
| `TriggerEvent.PlayerUseItem` | 玩家开始使用道具 | `eventobjid`, `itemid` | — |
| `TriggerEvent.PlayerChargeItemBegin` | 玩家开始蓄力道具 | `eventobjid`, `itemid` | — |
| `TriggerEvent.PlayerChargeItemEnd` | 玩家结束蓄力道具 | `eventobjid`, `itemid` | — |
| `TriggerEvent.PlayerConsumeItem` | 玩家消耗道具 | `eventobjid`, `itemid`, `itemnum` | — |
| `TriggerEvent.PlayerPickUpItem` | 玩家拾取道具 | `eventobjid`, `itemid`, `itemnum` | — |
| `TriggerEvent.PlayerDiscardItem` | 玩家丢弃道具 | `eventobjid`, `itemid`, `itemnum` | — |

### 4.7 玩家背包/快捷栏/装备事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.PlayerShortcutChange` | 快捷栏改变 | `eventobjid`, `ShortCutIdx`, `itemid` | — |
| `TriggerEvent.PlayerShortcutAddItem` | 快捷栏放入道具 | `eventobjid` | — |
| `TriggerEvent.PlayerShortcutRemItem` | 快捷栏取出道具 | `eventobjid` | — |
| `TriggerEvent.PlayerBackPackChange` | 背包栏改变 | `eventobjid`, `itemid` | — |
| `TriggerEvent.PlayerBackPackAddItem` | 背包栏放入道具 | `eventobjid` | — |
| `TriggerEvent.PlayerBackPackRemItem` | 背包栏取出道具 | `eventobjid` | — |
| `TriggerEvent.PlayerEquipChange` | 装备栏改变 | `eventobjid`, `itemid` | — |
| `TriggerEvent.PlayerEquipAddItem` | 装备栏放入道具 | `eventobjid` | — |
| `TriggerEvent.PlayerEquipRemItem` | 装备栏取出道具 | `eventobjid` | — |
| `TriggerEvent.PlayerEquipOn` | 玩家穿上装备 | `eventobjid`, `itemid` | — |
| `TriggerEvent.PlayerEquipOff` | 玩家脱下装备 | `eventobjid`, `itemid` | — |

### 4.8 玩家界面事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.PlayerOpenInnerView` | 打开游戏内部页面 | `eventobjid`, `CustomUI` | — |
| `TriggerEvent.PlayerCloseInnerView` | 关闭游戏内部页面 | `eventobjid`, `CustomUI` | — |

### 4.9 玩家战斗事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.PlayerBeHurt` | 玩家受到伤害 | `eventobjid`, `hurtlv`, `toobjid` | — |
| `TriggerEvent.PlayerDie` | 玩家被击败 | `eventobjid` | — |
| `TriggerEvent.PlayerAttack` | 玩家开始攻击 | `eventobjid` | — |
| `TriggerEvent.PlayerAttackHit` | 玩家攻击命中 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.PlayerDefeatActor` | 玩家击败目标 | `eventobjid`, `toobjid`, `targetactorid`（目标类型） | — |
| `TriggerEvent.PlayerDamageActor` | 玩家造成伤害 | `eventobjid`, `toobjid`, `hurtlv` | — |
| `TriggerEvent.PlayerAddBuff` | 玩家获得状态 | `eventobjid`, `buffid` | — |
| `TriggerEvent.PlayerRemoveBuff` | 玩家失去状态 | `eventobjid`, `buffid` | — |
| `TriggerEvent.PlayerChangeAttr` | 玩家属性改变 | `eventobjid`, `playerattr`, `playerattrval` | `RoleAttr.xxx` |
| `TriggerEvent.PlayerAttrStateChange` | 玩家权限改变 | `eventobjid`, `attstateType`, `attstateValue` | `Ability.xxx` |
| `TriggerEvent.PlayerMountActor` | 玩家骑乘坐骑 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.PlayerDismountActor` | 玩家取消骑乘 | `eventobjid`, `toobjid` | — |

### 4.10 生物战斗事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.MobBeHurt` | 生物受到伤害 | `eventobjid`, `actorid`（生物类型）, `hurtlv`, `toobjid` | — |
| `TriggerEvent.MobDie` | 生物被击败 | `eventobjid`, `actorid`, `toobjid` | — |
| `TriggerEvent.MobAttack` | 生物开始攻击 | `eventobjid`, `actorid`, `toobjid` | — |
| `TriggerEvent.MobAttackHit` | 生物攻击命中 | `eventobjid`, `actorid`, `toobjid` | — |
| `TriggerEvent.MobBeat` | 生物击败目标 | `eventobjid`, `actorid`, `toobjid` | — |
| `TriggerEvent.MobDamage` | 生物造成伤害 | `eventobjid`, `actorid`, `toobjid`, `hurtlv` | — |
| `TriggerEvent.MobAddBuff` | 生物获得状态 | `eventobjid`, `actorid`, `buffid` | — |
| `TriggerEvent.MobRemoveBuff` | 生物失去状态 | `eventobjid`, `actorid`, `buffid` | — |
| `TriggerEvent.MobChangeAttr` | 生物属性改变 | `eventobjid`, `actorid`, `actorattr`, `actorattrval` | `RoleAttr.xxx` |
| `TriggerEvent.MobAttrStateChange` | 生物权限改变 | `eventobjid`, `attstateType`, `attstateValue` | `Ability.xxx` |
| `TriggerEvent.MobMountActor` | 生物骑乘坐骑 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.MobDismountActor` | 生物取消骑乘 | `eventobjid`, `toobjid` | — |

### 4.11 角色通用事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.ActorPickupActor` | 角色举起角色 | `eventobjid`, `toobjid`, `pickupType` | — |

### 4.12 方块事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.BlockAdd` | 方块被创建 | `blockid`（方块类型）, `x,y,z` | — |
| `TriggerEvent.BlockRemove` | 方块被破坏 | `blockid`, `x,y,z` | — |
| `TriggerEvent.BlockDigBegin` | 方块开始被挖掘 | `blockid`, `x,y,z`, `eventobjid` | — |
| `TriggerEvent.BlockDigEnd` | 方块挖掘完毕 | `blockid`, `x,y,z`, `actorid`（生物类型） | — |
| `TriggerEvent.BlockDigCancel` | 方块挖掘中断 | `blockid`, `x,y,z`, `actorid` | — |
| `TriggerEvent.BlockTrigger` | 方块开关状态改变 | `blockid`, `x,y,z` | — |
| `TriggerEvent.BlockChangeColor` | 方块颜色改变 | `blockid`, `x,y,z` | — |
| `TriggerEvent.BlockChangeDir` | 方块方向改变 | `blockid`, `x,y,z` | — |
| `TriggerEvent.BlockContainerChange` | 储存容器改变 | `blockid`, `itemid`, `x,y,z` | — |
| `TriggerEvent.BlockContainerPutIn` | 容器放入道具 | `blockid`, `itemid`, `itemnum`, `x,y,z` | — |
| `TriggerEvent.BlockContainerTakeOut` | 容器取出道具 | `blockid`, `itemid`, `itemnum`, `x,y,z` | — |

### 4.13 UI/界面事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.UILostFocus` | 玩家在界面输入字符串 | `eventobjid`, `uielement`, `content` | — |
| `TriggerEvent.UISpineComplete` | 元件动画播放完毕 | `eventobjid`, `uielement` | — |
| `TriggerEvent.UIShow` | 界面被打开 | `eventobjid`, `CustomUI` | `uiid` |
| `TriggerEvent.UIHide` | 界面被关闭 | `eventobjid`, `CustomUI` | `uiid` |
| `TriggerEvent.UIButtonClick` | 元件被点击 | `eventobjid`, `uielement` | `elementid` |
| `TriggerEvent.UIButtonTouchBegin` | 元件被按下 | `eventobjid`, `uielement` | `elementid` |
| `TriggerEvent.UIButtonTouchEnd` | 元件被抬起 | `eventobjid`, `uielement` | `elementid` |
| `TriggerEvent.UIButtonLongPress` | 元件被长按 | `eventobjid`, `uielement` | `elementid` |
| `TriggerEvent.UIGLoader3DTouchClick` | 3D装载器被点击 | `eventobjid`, `uielement` | `elementid` |
| `TriggerEvent.UIGLoader3DTouchBegin` | 3D装载器被按下 | `eventobjid`, `uielement` | `elementid` |
| `TriggerEvent.UIGLoader3DTouchEnd` | 3D装载器被抬起 | `eventobjid`, `uielement` | `elementid` |
| `TriggerEvent.UIGLoader3DLongPress` | 3D装载器被长按 | `eventobjid`, `uielement` | `elementid` |
| `TriggerEvent.UIScrollPaneTouchBegin` | 滚动条触摸开始 | `eventobjid`, `uielement` | `elementid` |
| `TriggerEvent.UIScrollPaneTouchEnd` | 滚动条触摸结束 | `eventobjid`, `uielement` | `elementid` |
| `TriggerEvent.UIScrollPaneScrollEnd` | 滚动条惯性滑动结束 | `eventobjid`, `uielement` | `elementid` |

### 4.14 碰撞事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.PlayerCollideToPlayer` | 玩家与玩家碰撞 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.PlayerCollideToMob` | 玩家与生物碰撞 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.PlayerCollideToMissile` | 玩家与投掷物碰撞 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.PlayerCollideToDropItem` | 玩家与掉落物碰撞 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.PlayerCollideToEntity` | 玩家与实体碰撞 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.PlayerCollideToAreaObj` | 玩家与区域碰撞 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.MobCollideToPlayer` | 生物与玩家碰撞 | `eventobjid`, `actorid`（生物类型）, `toobjid` | — |
| `TriggerEvent.MobCollideToMob` | 生物与生物碰撞 | `eventobjid`, `actorid`, `toobjid` | — |
| `TriggerEvent.MobCollideToMissile` | 生物与投掷物碰撞 | `eventobjid`, `actorid`, `toobjid` | — |
| `TriggerEvent.MobCollideToDropItem` | 生物与掉落物碰撞 | `eventobjid`, `actorid`, `toobjid` | — |
| `TriggerEvent.MobCollideToEntity` | 生物与实体碰撞 | `eventobjid`, `actorid`, `toobjid` | — |
| `TriggerEvent.MobCollideToAreaObj` | 生物与区域碰撞 | `eventobjid`, `actorid`, `toobjid` | — |
| `TriggerEvent.MissileCollideToPlayer` | 投掷物与玩家碰撞 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.MissileCollideToMob` | 投掷物与生物碰撞 | `eventobjid`, `actorid`, `toobjid` | — |
| `TriggerEvent.DropItemCollideToPlayer` | 掉落物与玩家碰撞 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.DropItemCollideToMob` | 掉落物与生物碰撞 | `eventobjid`, `actorid`, `toobjid` | — |
| `TriggerEvent.EntityCollideToPlayer` | 实体与玩家碰撞 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.EntityCollideToMob` | 实体与生物碰撞 | `eventobjid`, `actorid`, `toobjid` | — |

### 4.15 区域事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.PlayerAreaIn` | 玩家进入区域 | `eventobjid`, `areaid` | `areaid` |
| `TriggerEvent.PlayerAreaOut` | 玩家离开区域 | `eventobjid`, `areaid` | `areaid` |
| `TriggerEvent.MobAreaIn` | 生物进入区域 | `eventobjid`, `areaid` | `areaid` |
| `TriggerEvent.MobAreaOut` | 生物离开区域 | `eventobjid`, `areaid` | `areaid` |
| `TriggerEvent.MissileAreaIn` | 投掷物进入区域 | `eventobjid`, `areaid` | `areaid` |
| `TriggerEvent.MissileAreaOut` | 投掷物离开区域 | `eventobjid`, `areaid` | `areaid` |
| `TriggerEvent.DropItemAreaIn` | 掉落物进入区域 | `eventobjid`, `areaid` | `areaid` |
| `TriggerEvent.DropItemAreaOut` | 掉落物离开区域 | `eventobjid`, `areaid` | `areaid` |
| `TriggerEvent.EntityAreaIn` | 实体进入区域 | `eventobjid`, `areaid` | `areaid` |
| `TriggerEvent.EntityAreaOut` | 实体离开区域 | `eventobjid`, `areaid` | `areaid` |
| `TriggerEvent.AreaObjAreaIn` | 区域进入区域 | `eventobjid`, `areaid` | `areaid` |
| `TriggerEvent.AreaObjAreaOut` | 区域离开区域 | `eventobjid`, `areaid` | `areaid` |

### 4.16 投掷物与掉落物事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.MissileCreate` | 投掷物创建 | `eventobjid`, `itemid` | — |
| `TriggerEvent.ProjectileHitBlock` | 投掷物击中方块 | `eventobjid`, `x,y,z` | — |
| `TriggerEvent.ProjectileHitPlayer` | 投掷物击中玩家 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.ProjectileHitMob` | 投掷物击中生物 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.ProjectileHitProj` | 投掷物击中投掷物 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.ProjectileHitItem` | 投掷物击中掉落物 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.ProjectileHitEntity` | 投掷物击中实体 | `eventobjid`, `toobjid` | — |
| `TriggerEvent.ItemCreate` | 掉落物创建 | `eventobjid`, `itemid`, `itemnum` | — |
| `TriggerEvent.DropItemPickup` | 掉落物被拾取 | `eventobjid`, `itemid`, `itemnum` | — |
| `TriggerEvent.ItemDisappear` | 掉落物消失 | `eventobjid`, `itemid` | — |

### 4.17 特效事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.ParticlePosOnCreate` | 特效创建在位置 | `effectid`, `x,y,z` | — |
| `TriggerEvent.ParticleObjectOnCreate` | 特效创建在对象 | `effectid`, `eventobjid` | — |
| `TriggerEvent.ParticlePlayerOnCreate` | 特效创建在玩家 | `effectid`, `eventobjid` | — |
| `TriggerEvent.ParticleMobOnCreate` | 特效创建在生物 | `effectid`, `eventobjid` | — |
| `TriggerEvent.ParticleProjectileOnCreate` | 特效创建在投掷物 | `effectid`, `eventobjid` | — |
| `TriggerEvent.ParticleItemOnCreate` | 特效创建在掉落物 | `effectid`, `eventobjid` | — |
| `TriggerEvent.ParticleEntityOnCreate` | 特效创建在实体 | `effectid`, `eventobjid` | — |

### 4.18 对象创建事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.MobCreate` | 生物被创建 | `eventobjid`, `actorid`（生物类型）, `x,y,z` | — |
| `TriggerEvent.EntityCreate` | 实体被创建 | `eventobjid`, `x,y,z` | — |
| `TriggerEvent.AreaObjCreate` | 区域被创建 | `eventobjid`, `x,y,z` | — |

### 4.19 配方与熔炼事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.CraftEnd` | 配方合成完毕 | `craftid`, `itemid`, `itemnum`, `x,y,z` | — |
| `TriggerEvent.FurnaceBegin` | 熔炼开始 | `furanceid`, `x,y,z` | — |
| `TriggerEvent.FurnaceEnd` | 熔炼结束 | `furanceid`, `x,y,z` | — |

### 4.20 开发者事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `TriggerEvent.DeveloperBuyItem` | 购买开发者商店道具 | `itemid`, `eventobjid` | — |


## 五、局部事件完整列表（ObjectEvent）

### 5.1 方块局部事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `ObjectEvent.BlockAdd` | 此类方块被创建 | `blockid`, `x,y,z` | — |
| `ObjectEvent.BlockClicked` | 此类方块被点击 | `eventobjid`（玩家实例）, `x,y,z` | — |
| `ObjectEvent.BlockRemove` | 此类方块被破坏 | `x,y,z` | — |
| `ObjectEvent.BlockDigBegin` | 此类方块开始被挖掘 | `eventobjid`, `x,y,z` | — |
| `ObjectEvent.BlockDigEnd` | 此类方块挖掘完毕 | `actorid`（生物类型）, `x,y,z` | — |
| `ObjectEvent.BlockDigCancel` | 此类方块挖掘中断 | `actorid`, `x,y,z` | — |
| `ObjectEvent.OnInteract` | 此类方块开关改变 | `x,y,z` | — |
| `ObjectEvent.BlockChangeColor` | 此类方块颜色改变 | `x,y,z` | — |
| `ObjectEvent.BlockChangeDir` | 此类方块方向改变 | `x,y,z` | — |
| `ObjectEvent.BlockContainerChange` | 此容器内容改变 | `itemid`, `x,y,z` | — |
| `ObjectEvent.BlockContainerPutIn` | 此容器放入道具 | `itemid`, `x,y,z` | — |
| `ObjectEvent.BlockContainerTakeOut` | 此容器取出道具 | `itemid`, `x,y,z` | — |

### 5.2 玩家局部事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `ObjectEvent.PlayerEnterGame` | 此玩家进入游戏 | `eventobjid` | — |
| `ObjectEvent.PlayerLeaveGame` | 此玩家离开游戏 | `eventobjid` | — |
| `ObjectEvent.PlayerVictory` | 此玩家游戏胜利 | `eventobjid` | — |
| `ObjectEvent.PlayerDefeat` | 此玩家游戏失败 | `eventobjid` | — |
| `ObjectEvent.PlayerRevive` | 此玩家复活 | `eventobjid`, `x,y,z` | — |
| `ObjectEvent.PlayerMoveOneBlockSize` | 此玩家移动 | `eventobjid`, `x,y,z` | — |
| `ObjectEvent.PlayerSelectShortcut` | 此玩家选中快捷栏 | `eventobjid`, `itemid`, `itemnum` | — |
| `ObjectEvent.PlayerInvateFriend` | 此玩家邀请好友 | `eventobjid`, `toobjid` | — |
| `ObjectEvent.PlayerNewInputContent` | 此玩家发送聊天 | `eventobjid`, `content` | — |
| `ObjectEvent.PlayerClickBlock` | 此玩家点击方块 | `blockid`（方块类型）, `x,y,z` | — |
| `ObjectEvent.PlayerClickPlayer` | 此玩家点击玩家 | `toobjid`（玩家实例） | — |
| `ObjectEvent.PlayerClickMob` | 此玩家点击生物 | `toobjid`（生物实例） | — |
| `ObjectEvent.PlayerClickProjectile` | 此玩家点击投掷物 | `toobjid` | — |
| `ObjectEvent.PlayerClickDropItem` | 此玩家点击掉落物 | `toobjid` | — |
| `ObjectEvent.PlayerClickEntity` | 此玩家点击实体 | `toobjid` | — |

### 5.3 玩家按键局部事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `ObjectEvent.PlayerInputKeyClick` | 此玩家点击按键 | `vkey` | `KeyCode.xxx` |
| `ObjectEvent.PlayerInputKeyDown` | 此玩家按下按键 | `vkey` | `KeyCode.xxx` |
| `ObjectEvent.PlayerInputKeyUp` | 此玩家抬起按键 | `vkey` | `KeyCode.xxx` |
| `ObjectEvent.PlayerInputKeyOnPress` | 此玩家长按按键 | `vkey` | `KeyCode.xxx` |

### 5.4 玩家道具局部事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `ObjectEvent.PlayerAddItem` | 此玩家获得道具 | `itemid`, `itemnum` | — |
| `ObjectEvent.PlayerUseItem` | 此玩家使用道具 | `itemid` | — |
| `ObjectEvent.PlayerChargeItemBegin` | 此玩家开始蓄力道具 | `itemid` | — |
| `ObjectEvent.PlayerChargeItemEnd` | 此玩家结束蓄力道具 | `itemid` | — |
| `ObjectEvent.PlayerConsumeItem` | 此玩家消耗道具 | `itemid`, `itemnum` | — |
| `ObjectEvent.PlayerPickUpItem` | 此玩家拾取道具 | `itemid`, `itemnum`, `toobjid` | — |

### 5.5 玩家背包/快捷栏/装备局部事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `ObjectEvent.PlayerShortcutChange` | 此玩家快捷栏改变 | `ShortCutIdx`, `itemid` | — |
| `ObjectEvent.PlayerShortcutAddItem` | 此玩家快捷栏放入道具 | — | — |
| `ObjectEvent.PlayerShortcutRemItem` | 此玩家快捷栏取出道具 | — | — |
| `ObjectEvent.PlayerBackPackChange` | 此玩家背包改变 | `ShortCutIdx`, `itemid` | — |
| `ObjectEvent.PlayerBackPackAddItem` | 此玩家背包放入道具 | — | — |
| `ObjectEvent.PlayerBackPackRemItem` | 此玩家背包取出道具 | — | — |
| `ObjectEvent.PlayerEquipChange` | 此玩家装备改变 | `ShortCutIdx`, `itemid` | — |
| `ObjectEvent.PlayerEquipAddItem` | 此玩家装备放入道具 | — | — |
| `ObjectEvent.PlayerEquipRemItem` | 此玩家装备取出道具 | — | — |
| `ObjectEvent.PlayerEquipOn` | 此玩家穿上装备 | `ShortCutIdx`, `itemid` | — |
| `ObjectEvent.PlayerEquipOff` | 此玩家脱下装备 | `ShortCutIdx`, `itemid` | — |

### 5.6 角色局部事件（Object 级别）

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `ObjectEvent.ObjectBeClick` | 此角色被玩家点击 | `toobjid`（点击者） | — |
| `ObjectEvent.ObjectBeHurt` | 此角色受到伤害 | `hurtlv`, `toobjid` | — |
| `ObjectEvent.ObjectDie` | 此角色被击败 | — | — |
| `ObjectEvent.ObjectAttack` | 此角色开始攻击 | — | — |
| `ObjectEvent.ObjectAttackHit` | 此角色攻击命中 | `toobjid` | — |
| `ObjectEvent.ObjectDefeat` | 此角色击败目标 | `toobjid` | — |
| `ObjectEvent.ObjectDamage` | 此角色造成伤害 | `toobjid`, `hurtlv` | — |
| `ObjectEvent.ObjectAddBuff` | 此角色获得状态 | `buffid` | — |
| `ObjectEvent.ObjectRemoveBuff` | 此角色失去状态 | `buffid` | — |
| `ObjectEvent.ObjectChangeAttr` | 此角色属性改变 | `playerattr`, `playerattrval` | `RoleAttr.xxx` |
| `ObjectEvent.ObjectAttrStateChange` | 此角色权限改变 | `attstateType`, `attstateValue` | `Ability.xxx` |
| `ObjectEvent.ObjectMountActor` | 此角色骑乘 | `toobjid` | — |
| `ObjectEvent.ObjectDismountActor` | 此角色取消骑乘 | `toobjid` | — |
| `ObjectEvent.ObjectMotionStateChange` | 此角色进入运动状态 | `playermotion` | `RoleMotion.xxx` |
| `ObjectEvent.ObjectMotionStateChangeEnd` | 此角色离开运动状态 | `playermotion` | `RoleMotion.xxx` |

### 5.7 角色碰撞局部事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `ObjectEvent.ObjectCollideByPlayer` | 此角色与玩家碰撞 | `toobjid` | — |
| `ObjectEvent.ObjectCollideByMob` | 此角色与生物碰撞 | `toobjid` | — |
| `ObjectEvent.ObjectCollideByMissile` | 此角色与投掷物碰撞 | `toobjid` | — |
| `ObjectEvent.ObjectCollideByDropItem` | 此角色与掉落物碰撞 | `toobjid` | — |
| `ObjectEvent.ObjectCollideByEntity` | 此角色与实体碰撞 | `toobjid` | — |
| `ObjectEvent.ObjectCollideByAreaObj` | 此角色与区域碰撞 | `toobjid` | — |

### 5.8 其他对象事件

| 事件名 | 说明 | 关键参数 | 可过滤 |
| :--- | :--- | :--- | :--- |
| `ObjectEvent.OnPropertyChange` | 组件属性改变 | 无 | — |
| `ObjectEvent.ObjectPlayAnim` | 对象播放动画 | `actorid` | — |


## 六、可过滤事件速查表

| 事件 | 过滤参数位置 | 可过滤值 |
| :--- | :--- | :--- |
| `TriggerEvent.PlayerInputKeyDown/Up/Click/OnPress` | 第3参数 | `KeyCode.xxx` |
| `TriggerEvent.PlayerMotionStateChange` | 第3参数 | `RoleMotion.xxx` |
| `TriggerEvent.PlayerMotionStateChangeEnd` | 第3参数 | `RoleMotion.xxx` |
| `TriggerEvent.PlayerChangeAttr` | 第3参数 | `RoleAttr.xxx` |
| `TriggerEvent.MobChangeAttr` | 第3参数 | `RoleAttr.xxx` |
| `TriggerEvent.PlayerGunAction` | 第3、4参数 | `GunState.xxx`, `GunAction.xxx` |
| `TriggerEvent.MinitimerChange` | 第3参数 | `timerid` |
| `TriggerEvent.PlayerAreaIn/Out` | 第3参数 | `areaid` |
| `TriggerEvent.MobAreaIn/Out` | 第3参数 | `areaid` |
| `TriggerEvent.MissileAreaIn/Out` | 第3参数 | `areaid` |
| `TriggerEvent.DropItemAreaIn/Out` | 第3参数 | `areaid` |
| `TriggerEvent.EntityAreaIn/Out` | 第3参数 | `areaid` |
| `TriggerEvent.UIButtonClick` | 第3参数 | `elementid` |
| `TriggerEvent.UIButtonTouchBegin/End` | 第3参数 | `elementid` |
| `TriggerEvent.UIButtonLongPress` | 第3参数 | `elementid` |
| `TriggerEvent.UIShow/Hide` | 第3参数 | `uiid` |
| `TriggerEvent.PlayerAttrStateChange` | 第3参数 | `Ability.xxx` |
| `TriggerEvent.MobAttrStateChange` | 第3参数 | `Ability.xxx` |
| `ObjectEvent.PlayerInputKeyDown/Up/Click/OnPress` | 第4参数（第3传nil） | `KeyCode.xxx` |
| `ObjectEvent.ObjectChangeAttr` | 第4参数（第3传nil） | `RoleAttr.xxx` |
| `ObjectEvent.ObjectAttrStateChange` | 第4参数（第3传nil） | `Ability.xxx` |
| `ObjectEvent.ObjectMotionStateChange` | 第4参数（第3传nil） | `RoleMotion.xxx` |


## 七、事件调用示例

### 7.1 全局事件示例（世界组件）

```lua
--[[
 * 脚本功能：玩家击杀计数器
--]]
local Script = {}

function Script:OnStart()
    self.cache = {}
    -- 监听玩家击败生物事件
    self:AddTriggerEvent(TriggerEvent.PlayerDefeatActor, self.OnDefeat)
    -- 监听玩家离开事件（清理缓存）
    self:AddTriggerEvent(TriggerEvent.GameAnyPlayerLeaveGame, self.OnLeave)
    -- 可选：监听按键测试
    self:AddTriggerEvent(TriggerEvent.PlayerInputKeyDown, self.OnKeyTest, KeyCode.F)
end

--- 玩家击败生物时触发
--- @param event table 事件数据，含 eventobjid（玩家实例）、toobjid（生物实例）
function Script:OnDefeat(event)
    local pid = event.eventobjid  -- 玩家实例ID
    local targetId = event.toobjid  -- 生物实例ID
    -- 击杀数变量ID（全局数值变量）
    local killVarId = "KILL_COUNT_VAR"
    if not self.cache[pid] then
        self.cache[pid] = Data:GetValue(killVarId, pid) or 0
    end
    self.cache[pid] = self.cache[pid] + 1
    Data:IncreasesValue(killVarId, pid, 1)
    print("玩家[" .. pid .. "]击败了生物[" .. targetId .. "]")
end

--- 玩家离开时清理缓存
function Script:OnLeave(event)
    self.cache[event.eventobjid] = nil
end

--- 按键测试
function Script:OnKeyTest(event)
    print("按下F键，当前击杀：" .. (self.cache[event.eventobjid] or 0))
end

return Script
```

### 7.2 局部事件示例（方块组件）

```lua
--[[
 * 脚本功能：点击方块替换为目标方块
--]]
local Script = {}

function Script:OnStart()
    -- 局部事件：仅监听挂载了此组件的方块类型
    self:AddEvent(ObjectEvent.BlockClicked, self.OnClick)
end

--- 方块被点击时触发
--- @param event table 事件数据，含 blockid（方块类型）、x,y,z（坐标）
function Script:OnClick(event)
    -- 目标方块ID（方块类型）
    local targetBlockId = 446  -- 紫荧矿石
    local success = Block:ReplaceBlock(targetBlockId, event.x, event.y, event.z)
    if success then
        print("方块已转换", event.x, event.y, event.z)
    end
end

return Script
```

### 7.3 UI组件事件示例（界面组件）

```lua
--[[
 * 脚本功能：UI界面交互
--]]
local Script = {}

-- 开放函数配置
Script.openFnArgs = {
    UpdateScore = true,
}

function Script:OnStart()
    -- 监听界面打开
    self:AddTriggerEvent(TriggerEvent.UIShow, self.OnUIShow, "ui_main")
    -- 监听按钮点击（过滤元件ID）
    self:AddTriggerEvent(TriggerEvent.UIButtonClick, self.OnBtnClick, "btn_start")
    -- 监听输入框失焦
    self:AddTriggerEvent(TriggerEvent.UILostFocus, self.OnInputLost, "input_name")
end

--- 界面打开时触发
function Script:OnUIShow(event)
    local pid = event.eventobjid
    CustomUI:SetText(pid, "ui_main", "txt_title", "欢迎回来！")
end

--- 按钮点击时触发
function Script:OnBtnClick(event)
    local pid = event.eventobjid
    CustomUI:SetText(pid, "ui_main", "txt_status", "游戏开始！")
end

--- 输入框失焦时触发
function Script:OnInputLost(event)
    local pid = event.eventobjid
    local name = event.content
    print("玩家[" .. pid .. "]输入了：" .. name)
end

--- 更新分数（开放函数）
function Script:UpdateScore(playerId, score)
    CustomUI:SetText(playerId, "ui_main", "txt_score", "分数：" .. score)
end

return Script
```

### 7.4 带 CurEventParam 的事件示例

```lua
--[[
 * 脚本功能：事件参数补充获取示例
--]]
local Script = {}

function Script:OnStart()
    self:AddTriggerEvent(TriggerEvent.PlayerBeHurt, self.OnPlayerHurt)
    self:AddTriggerEvent(TriggerEvent.PlayerAddBuff, self.OnPlayerAddBuff)
end

--- 玩家受到伤害时触发
--- @param event table 事件数据
function Script:OnPlayerHurt(event)
    -- 直接获取可能为 nil
    local hurt = event.hurtlv
    if hurt == nil then
        -- 使用 CurEventParam 补充获取
        local param = event.CurEventParam
        hurt = param.Hurtlv
    end
    local pid = event.eventobjid
    print("玩家[" .. pid .. "]受到伤害：" .. tostring(hurt))
end

--- 玩家获得状态时触发
function Script:OnPlayerAddBuff(event)
    local buffId = event.buffid
    if buffId == nil then
        local param = event.CurEventParam
        buffId = param.EventBuff
    end
    local pid = event.eventobjid
    print("玩家[" .. pid .. "]获得状态：" .. tostring(buffId))
end

return Script
```

### 7.5 带过滤参数的事件示例

```lua
--[[
 * 脚本功能：高效事件监听（带过滤）
--]]
local Script = {}

function Script:OnStart()
    -- 仅监听 Q 键按下
    self:AddTriggerEvent(TriggerEvent.PlayerInputKeyDown, self.OnQKey, KeyCode.Q)
    
    -- 仅监听血量变化
    self:AddTriggerEvent(TriggerEvent.PlayerChangeAttr, self.OnHpChange, RoleAttr.CurHp)
    
    -- 局部事件：仅监听血量变化（优先级传 nil）
    self:AddEvent(ObjectEvent.ObjectChangeAttr, self.OnObjHpChange, nil, RoleAttr.CurHp)
end

--- Q键按下时触发（已过滤）
function Script:OnQKey(event)
    print("按下了Q键，玩家ID：" .. event.eventobjid)
end

--- 玩家血量变化时触发（已过滤）
function Script:OnHpChange(event)
    print("玩家血量变化：" .. event.playerattrval)
end

--- 对象血量变化时触发（已过滤）
function Script:OnObjHpChange(event)
    print("对象血量变化：" .. event.playerattrval)
end

return Script
```


## 八、事件调试技巧

### 8.1 打印事件所有参数

```lua
function Script:OnEvent(event)
    -- 打印事件所有字段（调试用）
    for k, v in pairs(event) do
        if type(v) ~= "table" then
            print(k, "=", tostring(v))
        end
    end
    -- 如有 CurEventParam，也打印
    if event.CurEventParam then
        for k, v in pairs(event.CurEventParam) do
            print("CurEventParam." .. k, "=", tostring(v))
        end
    end
end
```

### 8.2 事件触发失败处理

> **如果事件触发不了/运行不了，优先使用 `CurEventParam` 替代直接参数获取。**

```lua
function Script:OnEvent(event)
    -- 直接获取可能为 nil
    local hurt = event.hurtlv
    -- 替代方案
    local param = event.CurEventParam
    hurt = hurt or param.Hurtlv
    -- 或直接使用 param
    local buffId = param.EventBuff
end
```


## 九、注意事项总结

1. **选择正确的接口**：全局事件用 `AddTriggerEvent`，局部事件用 `AddEvent`。
2. **区分 ID 类型**：`eventobjid`/`toobjid` 是实例 ID，`actorid`/`blockid`/`itemid` 是类型 ID。
3. **nil 参数规则**：中间的 `nil` 不可省略，末尾的 `nil` 可省略。
4. **事件过滤**：高频事件建议添加过滤参数，提升性能。
5. **CurEventParam**：当直接获取的参数为 `nil` 时，使用 `CurEventParam` 替代。
6. **ID 常量注释**：Data 相关 ID 必须注释说明含义和类型。
7. **注册时机**：事件监听在 `OnStart` 中注册。
8. **优先级参数**：`AddEvent` 的第3参数为优先级，不需要时传 `nil`（不可省略）。