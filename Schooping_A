from abc import ABC, abstractmethod

# --- 1. Abstraction (抽象) ---
class User(ABC):
    def __init__(self, name, password):
        self.name = name
        self.password = password  # 新增密碼屬性

    @abstractmethod
    def show_menu(self):
        """強制所有子類別必須實作自己的選單"""
        pass

# --- 2. Inheritance (繼承) & Encapsulation (封裝) ---
class Member(User):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.joined_group = None

    def leave_group(self):
        if hasattr(self, 'joined_group_obj') and self.joined_group_obj:
            target_group = self.joined_group_obj

            # 2. 從該小組的 members 清單中移除自己
            if self in target_group.members:
                target_group.members.remove(self)

            # 3. ✨ 關鍵：重置自己的所有小組屬性
            self.joined_group_obj = None  # 清除物件引用
            if hasattr(self, 'joined_group'):
                self.joined_group = ""    # 清除舊邏輯的字串標記

            print(f"✅ 您已成功退出小組：{target_group.name}")
        else:
            print("⚠️ 您目前不在任何小組中。")

    def show_menu(self):
        print(f"\n--- 組員 {self.name} 的選單 ---")
        print("1. 瀏覽小組並申請加入")
        print("2. 查看已加入的小組狀態")
        print("3. 退出目前小組")
        print("0. 登出")

    def apply_to_group(self, group_list):
        # 1. 檢查是否已經在「某個」小組內 (已現有的檢查)
        if getattr(self, 'joined_group_obj', None) is not None:
            print("❌ 您已經加入小組，無法再申請！")
            return

        if not group_list:
            print("目前沒有任何小組。")
            return

        print("\n可用小組清單：")
        for i, g in enumerate(group_list):
            print(f"[{i}] {g.name} - 介紹: {g.description} ({len(g.members)}/8人)")

        try:
            choice = int(input("請輸入想加入的小組編號: "))
            target_group = group_list[choice]

            # 2. ✨ 新增檢查：是否已經在該小組的待處理名單中
            if self in target_group.pending_requests:
                print(f"⚠️ 您已經申請過 '{target_group.name}'，請耐心等待組長審核。")
                return

            # 3. 執行申請
            target_group.add_to_pending(self)

        except (ValueError, IndexError):
            print("❌ 無效的編號，請重新嘗試。")

class Leader(Member): # 組長繼承組員，擁有組員所有功能
    def __init__(self, name, password):
        super().__init__(name, password)
        self.managed_group = None

    # --- 3. Polymorphism (多型) ---
    def show_menu(self):
        print(f"\n--- 組長 {self.name} 的管理選單 ---")
        print("1. 審核加入申請")
        print("2. 查看小組成員名單")
        print("3. 解散小組")
        print("0. 登出")

    def dismiss_group(self, all_groups):
        if self.managed_group:
            target_group = self.managed_group
            # 讓所有成員恢復單身
            for m in target_group.members:
                m.joined_group_obj = None
            self.managed_group = None
            all_groups.remove(target_group)
            print(f"✅ 小組 {target_group.name} 已解散。")
            return True
        return False

class Group:
    def __init__(self, name, description, leader, contact):
        self.name = name
        self.description = description
        self.leader = leader
        self.contact = contact
        self.members = [leader]
        self.pending_requests = []
        self.__MAX_SIZE = 8 # 封裝：不允許外部直接修改上限

    def add_to_pending(self, user):
        if len(self.members) < self.__MAX_SIZE:
            self.pending_requests.append(user)
            print(f"✅ 已發送申請至 {self.name}")
        else:
            print("❌ 該小組已滿！")

    def show_status(self):
        """這是在 Class 內部定義的方法"""
        print("\n" + "="*30)
        print(f"📊 小組狀態：{self.name}")
        print(f"📝 小組介紹：{self.description}")
        print(f"📞 聯絡方式：{self.contact}")
        print("-" * 30)
        print(f"👥 成員名單 ({len(self.members)}/8):")
        for i, m in enumerate(self.members):
            role_tag = " [組長]" if i == 0 else " [組員]"
            print(f"   {i+1}. {m.name}{role_tag}")
        print("="*30)

# --- 4. 主程式邏輯 (Main Loop) ---
def main():
    all_groups = []
    user_db = {}  # 儲存 {姓名: 密碼}


    # --- 💉 測試種子資料開始 (Seeding Data) ---
    # 1. 建立一個預設組長帳號
    test_leader_name = "Boss"
    user_db[test_leader_name] = "123"
    test_leader = Leader(test_leader_name, "123")

    # 2. 建立一個預設小組並綁定給該組長
    test_group = Group("Python開發組", "用來測試的模擬小組", test_leader, "WhatsApp:12345678")
    test_leader.managed_group = test_group
    all_groups.append(test_group)

    # 3. 建立一個預設組員帳號 (尚未加入組)
    test_member_name = "Kwan"
    user_db[test_member_name] = "123"

    # --- 💉 測試種子資料結束 ---



    while True:
        print("\n" + "="*30)
        print("   歡迎使用 COMP2090 分組管理系統")
        print("="*30)
        print("1. 註冊帳號")
        print("2. 登入系統")
        print("0. 關閉程式")

        entry_choice = input("請選擇操作: ")

        if entry_choice == "0":
            print("系統已關閉。")
            break

        # --- 1. 註冊邏輯 ---
        if entry_choice == "1":
            name = input("請輸入新使用者名稱: ")
            if name in user_db:
                print("❌ 該名稱已被使用，請換一個。")
                continue
            password = input("請設定密碼: ")
            user_db[name] = password
            print(f"🎉 註冊成功！歡迎 {name}。請重新選擇登入。")
            continue

        # --- 2. 登入邏輯 ---
        elif entry_choice == "2":
            name = input("使用者名稱: ")
            password = input("密碼: ")

            if name not in user_db or user_db[name] != password:
                print("❌ 名稱不存在或密碼錯誤！")
                continue

            print(f"✅ 登入成功！歡迎回來 {name}。")

            # --- 身分判定與物件檢索 ---
            # 檢查此人是否已經在某個組裡（無論是組長還是成員）
            current_group = None
            user = None
            role_choice = None

            for g in all_groups:
                # 檢查是否為組長
                if g.leader.name == name:
                    current_group = g
                    user = g.leader
                    role_choice = "1"
                    break
                # 檢查是否為組員
                elif any(m.name == name for m in g.members):
                    current_group = g
                    user = next(m for m in g.members if m.name == name)
                    role_choice = "2"
                    break

            # --- 若沒在任何組內，則選擇本次登入身分 ---
            if not current_group:
                print("ℹ️ 您目前沒有加入任何小組。")
                role_choice = input("請選擇本次登入身分：(1)創建小組 [組長] (2)加入小組 [組員]: ")

                if role_choice == "1":
                    user = Leader(name, password)
                    g_name = input("請輸入小組名稱: ")
                    g_desc = input("請輸入小組介紹: ")
                    g_contact = input("請輸入聯絡方式 (如TG/WhatsApp/Email): ")
                    new_group = Group(g_name, g_desc, user, g_contact1)
                    all_groups.append(new_group)
                    user.managed_group = new_group
                    print(f"🎉 小組 '{g_name}' 創建成功！")
                else:
                    user = Member(name, password)
            else:
                tag = "組長" if role_choice == "1" else "組員"
                print(f"📍 您目前以 [{tag}] 身分處於小組 '{current_group.name}' 中。")

            # --- 3. 內層功能選單 ---
            while True:
                user.show_menu()
                choice = input("請選擇功能 (0.登出): ")

                if choice == "0":
                    print(f"👋 {name} 已登出。")
                    break

                # --- 組員邏輯 ---
                if role_choice == "2":
                    if choice == "1":
                      # 檢查組員物件內是否有加入紀錄
                        if (hasattr(user, 'joined_group_obj') and user.joined_group_obj) or \
                          (hasattr(user, 'joined_group') and user.joined_group):
                          print("❌ 你已經加入小組，若想加入其他小組請先退出目前的小組。")
                          continue
                        user.apply_to_group(all_groups)
                    elif choice == "2":
                        # 顯示目前小組狀態
                        if hasattr(user, 'joined_group_obj') and user.joined_group_obj:
                            user.joined_group_obj.show_status()
                        elif hasattr(user, 'joined_group') and user.joined_group: # 相容舊程式碼
                             # 尋找對應的物件
                             for g in all_groups:
                                 if g.name == user.joined_group:
                                     g.show_status()
                                     break
                        else:
                            print("ℹ️ 尚未加入小組或申請尚在審核中。")
                    elif choice == "3":
                        if hasattr(user, 'leave_group'):
                            user.leave_group()
                        else:
                            print("⚠️ 尚未實作退出功能。")

                # --- 組長邏輯 ---
                elif role_choice == "1":
                    group = user.managed_group
                    if choice == "1": # 審核
                        if not group.pending_requests:
                            print("\n🔔 目前沒有待處理的申請。")
                        else:
                            print(f"\n--- 審核 {group.name} 的申請 ---")
                            for applicant in list(group.pending_requests):
                                ans = input(f"同意 {applicant.name} 加入？(y/n): ")
                                if ans.lower() == 'y':
                                  group.members.append(applicant)
                                  applicant.joined_group_obj = group  # 存物件
                                  applicant.joined_group = group.name # 存名字 (相容舊邏輯)
                                  print(f"✅ 已批准 {applicant.name}。")

                                group.pending_requests.remove(applicant)
                    elif choice == "2":
                        group.show_status()
                    elif choice == "3":
                        confirm = input("確定要解散小組嗎？此操作不可恢復 (y/n): ")
                        if confirm.lower() == 'y':
                            if user.dismiss_group(all_groups):
                                # ✨ 關鍵修改：
                                # 1. 強制更新當前身分為「無小組」狀態
                                current_group = None
                                role_choice = None

                                # 2. 重新詢問身分 (這段代碼直接複製你登入後的那段)
                                print("\nℹ️ 小組已解散，請重新選擇身分。")
                                role_choice = input("請選擇：(1)創建小組 (2)加入小組: ")

                                if role_choice == "1":
                                    # 重新執行創建邏輯...
                                    g_name = input("請輸入新小組名稱: ")
                                    g_desc = input("請輸入介紹: ")
                                    g_contact = input("請輸入聯絡方式: ")
                                    new_group = Group(g_name, g_desc, user, g_contact)
                                    all_groups.append(new_group)
                                    user.managed_group = new_group
                                    # 這裡不用 break，直接繼續 while 迴圈就會換成新選單
                                else:
                                    # 轉為普通組員物件
                                    user = Member(user.name, user.password)
                                    # 繼續迴圈

                                continue # 跳過本次迴圈剩餘部分，直接顯示新選單
                    else:
                      print("⚠️ 無效的選項，請重新輸入。")
if __name__ == "__main__":
    main()

