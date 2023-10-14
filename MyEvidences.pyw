from ttkbootstrap import *
from pyperclip import copy


class TeamspeakMenu:
    def __init__(self):
        self.font = "Calibri 12"
        self.optionsFrame = Frame(root)
        self.labelFrame = Frame(self.optionsFrame)
        self.entryFrame = Frame(self.optionsFrame)
        self.savePFrame = Frame(root)
        self.optionsFrame.pack()
        self.labelFrame.pack(side='left')
        self.entryFrame.pack(side='left')
        self.savePFrame.pack(pady=5)

        self.ignLabel = Label(self.labelFrame, text="IGN:", font=self.font)
        self.ign = Entry(self.entryFrame, font=self.font)

        self.reasonLabel = Label(self.labelFrame, text="Reason:", font=self.font)
        self.reason = Entry(self.entryFrame, font=self.font)

        self.proofsLabel = Label(self.labelFrame, text="Proofs:", font=self.font)
        self.proofs = Entry(self.entryFrame, font=self.font)

        self.copyButton = Button(self.savePFrame, text="Copy", bootstyle="succes", command=self.saveProof)

    def show(self):
        self.ignLabel.pack(side="top", pady=5)
        self.ign.pack(side="top")

        self.reasonLabel.pack(side="top", pady=5)
        self.reason.pack(side="top")

        self.proofsLabel.pack(side="top", pady=5)
        self.proofs.pack(side="top")

        self.copyButton.pack(side="bottom")

    def hide(self):
        self.ignLabel.destroy()
        self.ign.destroy()

        self.reasonLabel.destroy()
        self.reason.destroy()

        self.proofsLabel.destroy()
        self.proofs.destroy()
        self.labelFrame.destroy()
        self.entryFrame.destroy()
        self.savePFrame.destroy()
        self.copyButton.destroy()
        self.optionsFrame.destroy()

    def saveProof(self):
        ign = self.ign.get()
        reason = self.reason.get()
        proofs = self.proofs.get()
        copy(f"""[»] IGN: {ign} 
[»] Reason: {reason}
[»] Proof: {proofs}""")


class MuteMenu:
    def __init__(self):
        self.font = "Calibri 12"
        self.optionsFrame = Frame(root)
        self.labelFrame = Frame(self.optionsFrame)
        self.entryFrame = Frame(self.optionsFrame)
        self.savePFrame = Frame(root)
        self.optionsFrame.pack()
        self.labelFrame.pack(side='left')
        self.entryFrame.pack(side='left')
        self.savePFrame.pack(pady=5)

        self.ignLabel = Label(self.labelFrame, text="IGN:", font=self.font)
        self.ign = Entry(self.entryFrame, font=self.font)

        self.reasonLabel = Label(self.labelFrame, text="Reason:", font=self.font)
        self.reason = Entry(self.entryFrame, font=self.font)

        self.modalityLabel = Label(self.labelFrame, text="Modality:", font=self.font)
        self.modality = Entry(self.entryFrame, font=self.font)

        self.proofsLabel = Label(self.labelFrame, text="Proofs:", font=self.font)
        self.proofs = Entry(self.entryFrame, font=self.font)

        self.copyButton = Button(self.savePFrame, text="Copy", bootstyle="succes", command=self.saveProof)

    def show(self):
        self.ignLabel.pack(side="top", pady=5)
        self.ign.pack(side="top")

        self.reasonLabel.pack(side="top", pady=5)
        self.reason.pack(side="top")

        self.modalityLabel.pack(side="top", pady=5)
        self.modality.pack(side="top")

        self.proofsLabel.pack(side="top", pady=5)
        self.proofs.pack(side="top")

        self.copyButton.pack(side="bottom")

    def hide(self):
        self.ignLabel.destroy()
        self.ign.destroy()

        self.reasonLabel.destroy()
        self.reason.destroy()

        self.modalityLabel.destroy()
        self.modality.destroy()

        self.proofsLabel.destroy()
        self.proofs.destroy()
        self.labelFrame.destroy()
        self.entryFrame.destroy()
        self.savePFrame.destroy()
        self.copyButton.destroy()
        self.optionsFrame.destroy()

    def saveProof(self):
        ign = self.ign.get()
        reason = self.reason.get()
        proofs = self.proofs.get()
        modality = self.modality.get()
        copy(f"""[»] IGN: {ign} 
[»] Reason: {reason}
[»] Modality: {modality}
[»] Proof: {proofs}""")


class MainMenu:
    def __init__(self):
        self.mainTitleStr = StringVar()
        self.mainTitleStr.set("MainMenu")
        self.mainTitle = Label(root, textvariable=self.mainTitleStr, font="Calibri 25 bold")
        self.currentMenu = self
        self.mainTitle.pack(pady=10)

    def show(self):
        self.mainMenuFrame = Frame(root)
        self.teamspeakButton = Button(self.mainMenuFrame, text="Teamspeak", command=self.showTeamspeakEvidence)
        self.discordButton = Button(self.mainMenuFrame, text="Discord", command=self.showDiscordEvidence)
        self.banButton = Button(self.mainMenuFrame, text="Ban", command=self.showBanEvidence)
        self.muteButton = Button(self.mainMenuFrame, text="Mute", command=self.showMuteEvidence)
        self.warnButton = Button(self.mainMenuFrame, text="Warn", command=self.showWarnEvidence)
        self.tpHereButton = Button(self.mainMenuFrame, text="Tp Here", command=self.showTpHereEvidence)

        self.mainMenuFrame.pack(pady=2)
        self.teamspeakButton.pack(pady=2)
        self.discordButton.pack(pady=2)
        self.banButton.pack(pady=2)
        self.muteButton.pack(pady=2)
        self.warnButton.pack(pady=2)
        self.tpHereButton.pack(pady=2)

    def hide(self):
        self.mainMenuFrame.destroy()
        self.teamspeakButton.destroy()
        self.discordButton.destroy()
        self.banButton.destroy()
        self.muteButton.destroy()
        self.warnButton.destroy()
        self.tpHereButton.destroy()

    def showTeamspeakEvidence(self):
        self.hide()
        self.mainTitleStr.set("Teamspeak")
        self.currentMenu.hide()
        self.currentMenu = TeamspeakMenu()
        self.currentMenu.show()

    def showDiscordEvidence(self):
        self.hide()
        self.mainTitleStr.set("Discord")
        self.currentMenu.hide()
        self.currentMenu = TeamspeakMenu()
        self.currentMenu.show()

    def showBanEvidence(self):
        self.hide()
        self.mainTitleStr.set("Ban")
        self.currentMenu.hide()
        self.currentMenu = MuteMenu()
        self.currentMenu.show()

    def showMuteEvidence(self):
        self.hide()
        self.mainTitleStr.set("Mute")
        self.currentMenu.hide()
        self.currentMenu = MuteMenu()
        self.currentMenu.show()

    def showWarnEvidence(self):
        self.hide()
        self.mainTitleStr.set("Warn")
        self.currentMenu.hide()
        self.currentMenu = MuteMenu()
        self.currentMenu.show()

    def showTpHereEvidence(self):
        self.hide()
        self.mainTitleStr.set("Tp Here")
        self.currentMenu.hide()
        self.currentMenu = TeamspeakMenu()
        self.currentMenu.show()

    def showMenu(self):
        self.mainTitleStr.set("Main Menu")
        self.currentMenu.hide()
        self.currentMenu = self
        self.currentMenu.show()


root = Window(themename="darkly")
root.geometry("260x300")
root.title("EvidencesMenu")

menu = MainMenu()
menu.show()

backButton = Button(root, text="Back", bootstyle="danger", command=menu.showMenu)
backButton.pack(side="bottom")

root.mainloop()

